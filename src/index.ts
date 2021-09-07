import { PlayAudio } from "./functions/playAudio";
import schedule from "node-schedule";
import { fetchAPI } from "./functions/fetchAPI";
import { audio, audio1 } from "./config";
import { prayerList } from "./functions/prayerList";

(async () => {
  await PlayAudio(audio1);
  console.log("STARTED ADHAN APP");
  console.log(`--------------------------`);

  console.log(`DATE: ${new Date()}`);
  const currentTimes = await fetchAPI();
  await prayerList(currentTimes);

  schedule.scheduleJob("*/1 * * * *", async function () {
    console.log(`--------------------------`);
    console.log(`DATE: ${new Date()}`);

    const currentTimes = await fetchAPI();
    await prayerList(currentTimes);

    for (var i = 0; i < currentTimes.length; i++) {
      let currentTime = currentTimes[i].split(":");

      const currentHour: string = currentTime[0];
      const currentMin: string = currentTime[1];

      const hours: string = String(
        new Date().getHours() < 10
          ? `0${new Date().getHours()}`
          : new Date().getHours()
      );
      const minutes: string = String(
        new Date().getMinutes() < 10
          ? `0${new Date().getMinutes()}`
          : new Date().getMinutes()
      );

      if (currentHour === hours && currentMin === minutes) {
        console.log(`--------------------------`);
        console.log(`Time for Adhan`);
        console.log(`--------------------------`);
        await PlayAudio(audio);
      }
    }
  });
})();
