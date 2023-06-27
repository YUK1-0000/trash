use std::io::stdin;
use rand::Rng;

const HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main() {
    loop {
        let mut s = String::new();
        let mut retry = String::new();

        println!("\n1: {} 2: {} 3: {}", HANDS[0], HANDS[1], HANDS[2]);
        stdin().read_line(&mut s).unwrap();

        let i: usize = (s.replace("\n", "").parse::<u8>().unwrap() - 1).into();
        let j: usize = (rand::thread_rng().gen::<f32>() * 2.).round() as usize;

        let my_hand = HANDS[i];
        let cpu_hand = HANDS[j];

        println!("\nYou: {}\nCPU: {}", my_hand, cpu_hand);
        if j as i8 - 1 == i as i8 {
            println!("勝ち！");
        } else if i as i8 - 1 == j as i8 {
            println!("負け！");
        } else {
            println!("あいこ！");};
        
        println!("\n1: もう一回 2: やめる");
        stdin().read_line(&mut retry).unwrap();

        if retry.chars().next().unwrap().to_string() == "2" {
            break;
        };
    };
}