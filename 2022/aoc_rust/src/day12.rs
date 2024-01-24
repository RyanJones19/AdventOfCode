use std::env;
use std::fs;
use std::collections::HashSet;
use std::time::Instant;

struct Tuple {
    x: i32,
    y: i32,
    num_moves: i32
}

impl Tuple {
    fn new() -> Tuple {
        Tuple { x: 0, y: 0, num_moves: 0 }
    }
}

fn main() {
    let start_time = Instant::now();

    let args: Vec<String> = env::args().collect();

    let filename = &args[1];

    let contents = match fs::read_to_string(filename) {
        Ok(contents) => contents,
        Err(_) => panic!("Something went wrong reading the file")
    };

    let mut grid: Vec<Vec<u8>> = contents
        .lines()
        .map(|line| line.chars().map(|c| c as u8).collect())
        .collect();

    //let mut seen: HashSet<(i32, i32)> = HashSet::new();

    // Create a new tuple called start that contains x, y coordinates
    let mut start = Tuple::new();
    let mut end = Tuple::new();

    let height = grid.len() as i32;
    let width = grid[0].len() as i32;

    let mut all_starts: Vec<(i32, i32, i32)> = vec![];

    for (row_index, row) in grid.iter_mut().enumerate() {
        for (col_index, current_char) in row.iter_mut().enumerate() {
            let current_value = *current_char;
            if current_value == 83 {
                start = Tuple { x: row_index as i32, y: col_index as i32, num_moves: 0 };
                *current_char = std::u8::MAX;
            }
            if current_value == 69 {
                end = Tuple { x: row_index as i32, y: col_index as i32, num_moves: 0 };
            }
            if current_value == 97 {
                all_starts.push((row_index as i32, col_index as i32, 0));
            }
        }
    }

    all_starts.push((start.x, start.y, start.num_moves));

    //let mut possible_moves: Vec<(i32, i32, i32)> = vec![];//vec![(start.x, start.y, start.num_moves)];

    let mut min_moves = std::i32::MAX;

    for possible_start in all_starts {
        let mut possible_moves = vec![(possible_start.0, possible_start.1, possible_start.2)];
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        while possible_moves.len() > 0 {
            possible_moves.sort_by(|a, b| a.2.cmp(&b.2));
            let current_move = possible_moves.remove(0);
            if seen.contains(&(current_move.0, current_move.1)) {
                continue;
            }
            seen.insert((current_move.0, current_move.1));

            if current_move.0 == end.x && current_move.1 == end.y {
                if current_move.2 < min_moves {
                    min_moves = current_move.2;
                }
            }

            for (dx, dy) in [(-1,0), (1,0), (0,-1), (0,1)] {
                let newx = current_move.0 + dx;
                let newy = current_move.1 + dy;
                if 0<=newx && newx<height && 0<=newy && newy<width {
                    if i16::from(grid[current_move.0 as usize][current_move.1 as usize]) - i16::from(grid[newx as usize][newy as usize]) >= -1 {
                        if grid[newx as usize][newy as usize] == 69 {
                            if grid[current_move.0 as usize][current_move.1 as usize] == 122 {
                                possible_moves.push((newx, newy, current_move.2 + 1));
                            } else {
                                continue;
                            }
                        } else {
                            possible_moves.push((newx, newy, current_move.2 + 1));
                        }
                    }
                }
            }
        }
    }
    let end_time = Instant::now();
    println!("Part 2: {:?}", min_moves);
    println!("Runtime: {:?}", end_time - start_time);

}
