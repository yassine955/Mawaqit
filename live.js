const Audic = require("audic");

const mp3 = new Audic("https://server11.mp3quran.net/yasser/002.mp3");

return await mp3
  .play()
  .then(() => {
    console.log(`Audio is playing now!`);
  })
  .catch(console.error);
