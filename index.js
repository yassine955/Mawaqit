const fetch = require("node-fetch");
const cheerio = require("cheerio");
const player = require("play-sound")();
const path = require("path");
const cron = require("node-cron");

const playAudio = (filePath) => {
  player.play(filePath, (err) => {
    if (err) {
      console.error(`Failed to play audio: ${err.message}`);
      console.error(err.stack);
    }
  });
};

const fetchPrayers = async () => {
  const cookie = "currentCity=29263; Domain=www.al-yaqeen.com; Path=/";

  const res = await fetch("https://www.al-yaqeen.com/gebedstijden/", {
    headers: {
      Cookie: cookie,
    },
  })
    .then((res) => res.text())
    .then((data) => data);

  const $ = cheerio.load(res);
  const prayers = [];

  $("tr.prayer-table__day.current td").each((i, el) => {
    const time = $(el).text().trim();

    prayers.push(time);
  });

  return prayers;
};

// Schedule the task to run at 00:05 every day

cron.schedule("5 0 * * *", async () => {
  console.log("Fetching prayers...");
  const prayers = await fetchPrayers();
  console.log("Prayers:", prayers);

  // Check if local time is equal to one of the times in the prayers array
  const currentTime = new Date().toLocaleTimeString("en-US", { hour12: false });
  if (prayers.includes(currentTime)) {
    const audioFilePath = path.join(__dirname, "/adhan.mp3");
    playAudio(audioFilePath);
  }
});
