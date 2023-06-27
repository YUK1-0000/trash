use std::io::stdin;
use rand::Rng;

const HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main() {
    let mut win = 0;
    let mut lose = 0;
    let mut even = 0;
    for i in 1..=100000 {
        let mut s = String::new();
        let mut retry = String::new();


        println!("\n1: {} 2: {} 3: {}", HANDS[0], HANDS[1], HANDS[2]);
        //stdin().read_line(&mut s).unwrap();

        //let i: usize = (s.replace("\n", "").parse::<u8>().unwrap() - 1).into();
        let j: usize = (rand::thread_rng().gen::<f32>() * 2.).round() as usize;
        let i = 0;
        let my_hand = HANDS[i];
        let cpu_hand = HANDS[j];
        println!("j{}", j);
        println!("\nYou: {}\nCPU: {}\n", my_hand, cpu_hand);
        if j as i8 - 1 == i as i8 {
            println!("勝ち！");
            win += 1
        } else if j as i8 - 2 == i as i8 {
            println!("負け！");
            lose += 1
        } else {
            println!("あいこ！");
            even += 1
        };
        println!("\n{}勝{}敗{}分", win, lose, even);
        /* 
        println!("\n1: もう一回 2: やめる");
        stdin().read_line(&mut retry).unwrap();

        if retry.chars().next().unwrap().to_string() != "1" {
            break;
        };*/
    };
}