use std::io::{stdin, stdout};
use rand::Rng;

const HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main(){
    loop{
        let mut i = String::new();
        stdin().read_line(&mut i).unwrap();
        let j = (rand::thread_rng().gen::<f32>() * 2.).round() as u8;
        let my_hand = HANDS[0];
        let cpu_hand = HANDS[0];
        println!("You: {}\nCPU: {}\ni: {}\nj: {}", my_hand, cpu_hand, i, j);
        break;
    };
}