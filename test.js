// console.log([] + [])
// console.log([] + {})
// console.log(0.1 + 0.2 === 0.3)
// console.log({} + 10)

// const m = new Map();
// m["a"] = 10; // This does not add data to the Map internally, Instead, it adds a normal object property to the m object itself.
// m.set("b", 20);
// console.log(m.size); // 1

for (var i=0; i < 10; i++) {
    setTimeout(()=>{
        console.log(i)
    }, 1000);
}