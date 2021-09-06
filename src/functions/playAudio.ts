import Audic from "audic";

export const PlayAudio = async (audio: string) => {
  const mp3: Audic = new Audic(audio);

  return await mp3
    .play()
    .then(() => {
      console.log(`Audio is playing now!`);
    })
    .catch(console.error);
};
