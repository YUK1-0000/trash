use std::io::{stdin, stdout};
use rand::Rng;

const _HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main(){
    loop{
        let _cpu_hand = (rand::thread_rng().gen::<f32>() * 2.).round();
        let mut my_hand = String::new();
        stdin().read_line(&mut my_hand).unwrap();
        println!("{}", my_hand);
        break;
    };
}