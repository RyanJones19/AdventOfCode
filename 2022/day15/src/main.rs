use std::fs;
use std::env;
use regex::Regex;
use std::collections::HashSet;

#[derive(Debug)]
struct Tuple {
    sen_x: i32,
    sen_y: i32,
    bea_x: i32,
    bea_y: i32
}

fn manhattan_distance(point_1_x: i32, point_1_y: i32, point_2_x: i32, point_2_y: i32) -> i32 {
    (point_2_x - point_1_x).abs() + (point_2_y - point_1_y).abs()
}

fn is_valid_move(sensor_x: i32, sensor_y: i32, dx: i32, dy: i32, valid_distance: i32) -> bool {
    let new_distance = manhattan_distance(dx, dy, sensor_x, sensor_y);
    new_distance <= valid_distance
}

fn check_moves(sensor_x: i32, sensor_y: i32, current_x: i32, current_y: i32, valid_distance: i32, invalid_beacons: &mut HashSet<(i32,i32)>, seen: &mut HashSet<(i32,i32)>, beacons: &HashSet<(i32,i32)>) {
    for (dx, dy) in [(1,0), (0,1), (-1,0), (0,-1)] {
        if seen.contains(&(current_x + dx, current_y + dy)) {
            continue;
        }
        seen.insert((current_x + dx, current_y + dy));
        if is_valid_move(sensor_x, sensor_y, current_x + dx, current_y + dy, valid_distance) {
            if current_y + dy == 10 && !beacons.contains(&(current_x + dx, current_y + dy)){
                invalid_beacons.insert((current_x + dx, current_y + dy));
            }
            check_moves(sensor_x, sensor_y, current_x + dx, current_y + dy, valid_distance, invalid_beacons, seen, beacons);
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();

    let filename = &args[1];

    let mut sensors: Vec<Tuple> = Vec::new();

    let input: String = fs::read_to_string(filename).expect("Could not read input file");

    let lines: Vec<&str> = input.trim().split('\n').collect();
    let mut invalid_beacons: HashSet<(i32, i32)> = HashSet::new();
    let mut beacons: HashSet<(i32, i32)> = HashSet::new();

    let xre = Regex::new(r"x=(-?\d+)").expect("Failed to create x regex");
    let yre = Regex::new(r"y=(-?\d+)").expect("Failed to create y regex");

    for line in lines {
        let split_line: Vec<&str> = line.split(':').collect();
        let sensor_info = split_line[0];
        let beacon_info = split_line[1];
        let mut sensor_x_val: i32 = 0;
        let mut sensor_y_val: i32 = 0;
        let mut beacon_x_val: i32 = 0;
        let mut beacon_y_val: i32 = 0;

        if let Some(sensor_data) = xre.captures(sensor_info) {
            if let Some(x_data) = sensor_data.get(1) {
                sensor_x_val = x_data.as_str().parse::<i32>().expect("Failed to parse x value");
            }
        }

        if let Some(sensor_data) = yre.captures(sensor_info) {
            if let Some(y_data) = sensor_data.get(1) {
                sensor_y_val = y_data.as_str().parse::<i32>().expect("Failed to parse y value");
            }
        }

        if let Some(beacon_data) = xre.captures(beacon_info) {
            if let Some(x_data) = beacon_data.get(1) {
                beacon_x_val = x_data.as_str().parse::<i32>().expect("Failed to parse x value");
            }
        }

        if let Some(beacon_data) = yre.captures(beacon_info) {
            if let Some(y_data) = beacon_data.get(1) {
                beacon_y_val = y_data.as_str().parse::<i32>().expect("Failed to parse y value");
            }
        }

        let sensor_tuple = Tuple { sen_x: sensor_x_val, sen_y: sensor_y_val, bea_x: beacon_x_val, bea_y: beacon_y_val };

        sensors.push(sensor_tuple);
        beacons.insert((beacon_x_val, beacon_y_val));
    }

    for sensor in &sensors {
        let valid_distance = manhattan_distance(sensor.bea_x, sensor.bea_y, sensor.sen_x, sensor.sen_y);
        let mut seen: HashSet<(i32, i32)> = HashSet::new();
        seen.insert((sensor.sen_x, sensor.sen_y));
        check_moves(sensor.sen_x, sensor.sen_y, sensor.sen_x, sensor.sen_y, valid_distance, &mut invalid_beacons, &mut seen, &beacons);
    }

    println!("HashSet is: {:?}", invalid_beacons);
    println!("HashSet length is {:?}", invalid_beacons.len());

}
