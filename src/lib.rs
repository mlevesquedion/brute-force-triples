#[no_mangle]
pub extern "C" fn triples() {
    for i in 0..1000 {
        for j in (i + 1)..1000 {
            for k in (j + 1)..1000 {
                if i * i + j * j == k * k {
                    println!("({}, {}, {})", i, j, k);
                }
            }
        }
    }
}
