use std::fs;
use std::env;

#[derive(Debug)]
struct HBar {
    tile_1: (i32, i32)
}

fn main() {
    let input_args: Vec<String> = env::args().collect();
    let filename = &input_args[1];
    println!("{}", filename);

    let file_contents = fs::read_to_string(filename).expect("Could not read file");

    println!("{:?}", file_contents);

    let h_bar: HBar = HBar { tile_1: (1, 1)};

    println!("{:?}", h_bar.tile_1);

}
