use std::env;
use std::fs;
use std::cmp;
use std::time::Instant;

fn add_rocks(grid: &mut Vec<Vec<char>>, x: &u32, y: &u32, dx: &u32, dy: &u32, grid_floor: &mut u32) {
    *grid_floor = cmp::max(cmp::max(*y, *dy), *grid_floor);
    if x != dx {
        for i in cmp::min(*x, *dx)..cmp::max(*x, *dx)+1 {
            grid[*y as usize][i as usize] = '#';
        }
    } else {
        for i in cmp::min(*y, *dy)..cmp::max(*y, *dy)+1 {
            grid[i as usize][*x as usize] = '#';
        }
    }
}

fn drop_sand(grid: &mut Vec<Vec<char>>) -> (usize, usize, bool) {
    let mut new_sand = (0, 500, true);
    let grid_height = grid.len()-1;
    while new_sand.2 {
        if new_sand.0 == grid_height {
            new_sand = (grid_height, new_sand.1, false);
        }
        else if grid[new_sand.0 + 1][new_sand.1] == '.' {
            new_sand = (new_sand.0 + 1, new_sand.1, new_sand.2);
        }
        else if grid[new_sand.0 + 1][new_sand.1 -1] == '.' {
            new_sand = (new_sand.0 + 1, new_sand.1 - 1, new_sand.2);
        }
        else if grid[new_sand.0 + 1][new_sand.1 + 1] == '.' {
            new_sand = (new_sand.0 + 1, new_sand.1 + 1, new_sand.2);
        }
        else {
            new_sand = (new_sand.0, new_sand.1, false)
        }
    }
    return new_sand
}

fn main() {
    let start_time = Instant::now();

    let args: Vec<String> = env::args().collect();

    let mut grid: Vec<Vec<char>> = vec![vec!['.'; 1000]; 300];
    let mut grid_floor = 0;

    let rock_patterns:String = fs::read_to_string(&args[1]).expect("Something went wrong reading the file");

    for rock_pattern in rock_patterns.lines() {
        let rocks: Vec<&str> = rock_pattern.trim().split("->").collect();
        let mut iter = rocks.iter().peekable();
        while let Some(rock) = iter.next(){
            if let Some(next_rock) = iter.peek() {
                let mut coordinates = rock.split(",");
                let mut next_coordinates = next_rock.split(",");
                let x = coordinates.next().expect("expected an x coordinate").trim().parse::<u32>().expect("Could not convert to int");
                let y = coordinates.next().expect("expected a y coordinate").trim().parse::<u32>().expect("Could not convert to int");
                let dx = next_coordinates.next().expect("expected an x coordinate").trim().parse::<u32>().expect("Could not convert to int");
                let dy = next_coordinates.next().expect("expected a y coordinate").trim().parse::<u32>().expect("Could not convert to int");
                add_rocks(&mut grid, &x, &y, &dx, &dy, &mut grid_floor);
                
            }
        }
    }

    grid_floor += 2;
    grid[grid_floor as usize] = vec!['#'; 1000];
    let mut dropped_sand = 0;
    let mut sand = drop_sand(&mut grid);

    while grid[0][500] != '#' {
        dropped_sand += 1;
        grid[sand.0][sand.1] = '#';
        sand = drop_sand(&mut grid);
    }

    let end_time = Instant::now();
    println!("Part 2: {}", dropped_sand);
    println!("Runtime: {:?}", end_time - start_time);

}
