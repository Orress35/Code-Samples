fn get_divisors(n) {
    if (n <= 1) return 1;
    let divisors = 1;
    for (let i = 1; i <= n/2; i++) {
        if (n % i == 0) divisors++;
    }
    return divisors;
}

// driver code
fn main() {
    println!("divisors: {}", get_divisors(4324320));
}
