const Audic = require("audic");

export const PlayAudio = async (audio) => {
  const mp3 = new Audic(audio);

  return await mp3
    .play()
    .then(() => {
      console.log(`Audio is playing now!`);
    })
    .catch(console.error);
};
