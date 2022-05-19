const prayerList = require("./functions/prayerList");
const fetchAPI = require("./functions/fetchAPI");
const schedule = require("node-schedule");
const Audic = require("audic");
const path = require("path");

const audio = path.join(__dirname, "../src/sounds/adhan1.mp3");
const audio1 = path.join(__dirname, "../src/sounds/beep.mp3");

(async () => {
  const mp3 = new Audic(audio1);

  await mp3
    .play()
    .then(() => {
      console.log(`Audio is playing now!`);
    })
    .catch(console.error);

  console.log("STARTED ADHAN APP");
  console.log(`--------------------------`);

  console.log(`DATE: ${new Date()}`);
  const currentTimes = await fetchAPI.fetchAPI();
  await prayerList.prayerList(currentTimes);

  schedule.scheduleJob("*/1 * * * *", async function () {
    console.log(`--------------------------`);
    console.log(`DATE: ${new Date()}`);

    const currentTimes = await fetchAPI.fetchAPI();
    await prayerList.prayerList(currentTimes);

    for (var i = 0; i < currentTimes.length; i++) {
      let currentTime = currentTimes[i].split(":");

      const currentHour = currentTime[0];
      const currentMin = currentTime[1];

      const hours = String(
        new Date().getHours() < 10
          ? `0${new Date().getHours()}`
          : new Date().getHours()
      );
      const minutes = String(
        new Date().getMinutes() < 10
          ? `0${new Date().getMinutes()}`
          : new Date().getMinutes()
      );

      if (currentHour === hours && currentMin === minutes) {
        console.log(`--------------------------`);
        console.log(`Time for Adhan`);
        console.log(`--------------------------`);

        const mp3 = new Audic(audio);

        await mp3
          .play()
          .then(() => {
            console.log(`Audio is playing now!`);
          })
          .catch(console.error);
      }
    }
  });
})();
