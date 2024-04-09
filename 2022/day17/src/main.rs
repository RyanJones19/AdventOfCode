use std::fs;
use std::env;

#[derive(Debug)]
struct HBar {
    tile_1: (i32, i32),
    tile_2: (i32, i32),
    tile_3: (i32, i32),
    tile_4: (i32, i32),
    height: i32,
    points: Vec<(i32, i32)>,
    shape: String
}

impl HBar {
    fn new() -> Self {
        let mut h_bar = HBar {
            tile_1: (0, 2),
            tile_2: (0, 3),
            tile_3: (0, 4),
            tile_4: (0, 5),
            height: 1,
            points: Vec::new(),
            shape: "hbar".to_string()
        };
        h_bar.set_points();
        return h_bar;
    }

    fn set_points(&mut self) {
        self.points.push(self.tile_1);
        self.points.push(self.tile_2);
        self.points.push(self.tile_3);
        self.points.push(self.tile_4);
    }
}

#[derive(Debug)]
struct VBar {
    tile_1: (i32, i32),
    tile_2: (i32, i32),
    tile_3: (i32, i32),
    tile_4: (i32, i32),
    height: i32,
    points: Vec<(i32, i32)>,
    shape: String
}

impl VBar {
    fn new() -> Self {
        let mut v_bar = VBar {
            tile_1: (0, 2),
            tile_2: (1, 2),
            tile_3: (2, 2),
            tile_4: (3, 2),
            height: 1,
            points: Vec::new(),
            shape: "vbar".to_string()
        };
        v_bar.set_points();
        return v_bar;
    }

    fn set_points(&mut self) {
        self.points.push(self.tile_1);
        self.points.push(self.tile_2);
        self.points.push(self.tile_3);
        self.points.push(self.tile_4);
    }
}

#[derive(Debug)]
struct Game<T> {
    board: Vec<Vec<char>>,
    height: i32,
    active_points: Vec<(i32, i32)>,
    active_shape: T
}

impl<T> Game<T> {
    fn new(active_shape: T) -> Self {
        let mut game = Game {
            board: vec![vec!['_'; 7]],
            height: 1,
            active_points: Vec::new(),
            active_shape
        };
        return game;
    }
}

fn main() {
    let input_args: Vec<String> = env::args().collect();
    let filename = &input_args[1];
    println!("{}", filename);

    let file_contents = fs::read_to_string(filename).expect("Could not read file");

    println!("{:?}", file_contents);

    let h_bar: HBar = HBar::new();
    let v_bar: VBar = VBar::new();

    println!("{:?}", h_bar.points);

    let game: Game<HBar> = Game::new(h_bar);

    println!("{:?}", game.board);

    //game.active_shape = v_bar;

}
