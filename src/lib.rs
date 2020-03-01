#[no_mangle]
pub extern "C" fn triples() {
    for i in 1..2000 {
        for j in (i + 1)..2000 {
            let k = ((i * i + j * j) as f64).sqrt();
            if k.fract() == 0.0 {
                println!("({}, {}, {})", i, j, k.trunc());
            }
        }
    }
}
