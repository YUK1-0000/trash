use std::io::{stdin, stdout};
use rand::Rng;

const HANDS: [&str;3] = ["rock", "scissors", "paper"];


fn main(){
    loop{
        println!("Input 0 or 1 or 2");

        let mut s: String = String::new();
        stdin().read_line(&mut s).unwrap();

        let i: usize = s.replace("\n", "").parse().unwrap();
        let j: usize = (rand::thread_rng().gen::<f32>() * 2.).round() as usize;

        let my_hand = HANDS[i];
        let cpu_hand = HANDS[j];

        println!("You: {}\nCPU: {}", my_hand, cpu_hand);
        break
    };
}