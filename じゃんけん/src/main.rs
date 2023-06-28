use std::io::stdin;
use rand::Rng;

const HANDS: [&str;3] = ["グー", "チョキ", "パー"];


fn main() {
    let mut win = 0;
    let mut lose = 0;
    let mut win_streak = 0;
    let mut max_win_streak = 0;

    loop {
        let mut s = String::new();
        let mut retry = String::new();

        println!("\n1: {} 2: {} 3: {}", HANDS[0], HANDS[1], HANDS[2]);
        stdin().read_line(&mut s).unwrap();

        let i = (s.replace("\n", "").parse::<u8>().unwrap() - 1) as usize;
        let i = 0;
        let j = loop {
            let tmp = (rand::thread_rng().gen::<f32>() * 3.).floor() as usize;
            if tmp != 3 {
                break tmp
            };
        };

        let my_hand = HANDS[i];
        let cpu_hand = HANDS[j];

        println!("\nYou: {}\nCPU: {}\n", my_hand, cpu_hand);

        if j as i8 - 1 == i as i8 {
            println!("勝ち！");
            win_streak += 1;
            win += 1
        } else if j as i8 - 2 == i as i8 {
            println!("負け！");
            win_streak = 0;
            lose += 1
        } else {
            println!("あいこ！");
            continue
        };

        print!("\n{}勝{}敗", win, lose);
        if win_streak > 1 {
            println!("  {}連勝", win_streak)
        }
        println!("\n1: もう一回 2: やめる");
        stdin().read_line(&mut retry).unwrap();

        if retry.chars().next().unwrap().to_string() != "1" {
            break;
        };
    }
}