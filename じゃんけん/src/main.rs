use std::io::stdin;
use rand::Rng;

const HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main() {
    let mut win = 0;
    let mut lose = 0;
    let mut win_streak = 0;

    loop {
        let mut s = String::new();
        let mut retry = String::new();

        println!("\n1: {} 2: {} 3: {}", HANDS[0], HANDS[1], HANDS[2]);
        stdin().read_line(&mut s).unwrap();

        let i = s[..s.len()-1].parse::<i8>().unwrap() - 1;
        let j = loop {
            let tmp = (rand::thread_rng().gen::<f32>() * 3.).floor() as i8;
            if tmp != 3 { break tmp; };
        };

        let my_hand = HANDS[i as usize];
        let cpu_hand = HANDS[j as usize];

        println!("\nYou: {}\nCPU: {}\n", my_hand, cpu_hand);

        if j - 1 == i {
            println!("勝ち！");
            win_streak += 1;
            win += 1;
        } else if j - 2 == i {
            println!("負け！");
            win_streak = 0;
            lose += 1;
        } else {
            println!("あいこ！");
            continue;
        };

        print!("\n{}勝{}敗", win, lose);
        if win_streak > 1 {
            println!("  {}連勝", win_streak);
        };
        println!("\n1: もう一回 2: やめる");
        stdin().read_line(&mut retry).unwrap();

        if retry.chars().next().unwrap().to_string() != "1" {
            break;
        };
    };
}