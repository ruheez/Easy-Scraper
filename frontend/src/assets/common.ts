function randint(min = 0, max = 10) {
    return Math.floor(Math.random() * (+max - +min)) + +min
}

export { randint };
