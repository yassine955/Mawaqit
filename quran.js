const readline = require("readline");
const Audic = require("audic");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("Give me your link:", async function (name) {
  const mp3 = new Audic(name);

  return await mp3
    .play()
    .then(() => {
      console.log(`Audio is playing now!`);
    })
    .catch(console.error);
});

rl.on("close", function () {
  console.log("\nBYE BYE !!!");
  process.exit(0);
});
