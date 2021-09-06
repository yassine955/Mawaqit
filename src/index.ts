import path from "path";
import { PlayAudio } from "./functions/playAudio";
import schedule from "node-schedule";
import { fetchAPI } from "./functions/fetchAPI";

const audio: string = path.join(__dirname, "../src/sounds/adhan1.mp3");
const audio1: string = path.join(__dirname, "../src/sounds/beep.mp3");
export const PRAYERNAMES: string[] = [
  "Fajr",
  "Dhuhr",
  "'Asr",
  "Maghrib",
  "'Ishaa",
];

(async () => {
  await PlayAudio(audio1);
  console.log("STARTED ADHAN APP");
  console.log(`--------------------------`);
  console.log(`DATE: ${new Date()}`);
  const currentTimes = await fetchAPI();
  PRAYERNAMES.map((p, i) => {
    console.log(`${p}: ${currentTimes[i]}`);
  });
  schedule.scheduleJob("*/1 * * * *", async function () {
    console.log(`--------------------------`);
    console.log(`DATE: ${new Date()}`);
    const currentTimes = await fetchAPI();
    PRAYERNAMES.map((p, i) => {
      console.log(`${p}: ${currentTimes[i]}`);
    });

    for (var i = 0; i < currentTimes.length; i++) {
      if (i !== 1) {
        let currentTime = currentTimes[i].split(":");
        let hours: string = String(
          new Date().getHours() < 10
            ? `0${new Date().getHours()}`
            : new Date().getHours()
        );
        let minutes: string = String(
          new Date().getMinutes() < 10
            ? `0${new Date().getMinutes()}`
            : new Date().getMinutes()
        );

        const currentHour: string = currentTime[0];
        const currentMin: string = currentTime[1];

        if (currentHour === hours && currentMin === minutes) {
          console.log(`--------------------------`);
          console.log(`Time for Adhan`);
          console.log(`--------------------------`);
          await PlayAudio(audio);
        }
      }
    }
  });
})();
