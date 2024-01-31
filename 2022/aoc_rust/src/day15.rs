use std::fs;
use std::env;
use std::collections::HashSet;
use regex::Regex;

struct Tuple {
    x: i32,
    y: i32
}

impl Tuple {
    fn new() -> Tuple {
        return Tuple { x: 0, y: 0}
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];

    println!("{}", filename);

    let mut beacons: HashSet<Tuple> = HashSet::new();

    let input: String = fs::read_to_string(filename).expect("Could not read input file");

    let lines: Vec<&str> = input.split('\n').collect();

    let xre = Regex::new(r"x=(\d+)").expect("Failed to create regex");

    for line in lines {
        let mut splitLine: Vec<&str> = line.split(':').collect();
        let mut sensor_info = splitLine[0];
        let mut beacon_info = splitLine[1];
        println!("{}", sensor_info);
        println!("{}", beacon_info);
        if let Some(captures) = xre.captures(sensor_info) {
            if let Some(x_value) = captures.get(0) {
                let x: i32 = x_value.as_str().parse().expect("Failed to parse x value");
                println!("Captured x value: {}", x);
            }
        }
    }

    /*for sensor in sensors {
        println!("{}", sensor);
    }
    for beacon in beacons {
        println!("{:?}", beacon);
    }*/

}
