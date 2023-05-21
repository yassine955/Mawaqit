import puppeteer from "puppeteer";
import cron from "node-cron";
import path from "path";
import soundPlay from "sound-play";

let prayerTimes: (string | null)[] = [];

async function firstTimeStart() {
  try {
    console.log(`Audio is playing now!`);

    await soundPlay.play(path.join(__dirname, "../src/audio/beep.mp3"), 1);
  } catch (error) {
    console.error("Error playing audio:", error);
  }
}

(async () => {
  await firstTimeStart();

  async function scrapePrayerTimes() {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    await page.goto("https://mawaqit.net/nl/alhijra-leiden");

    // Wait for the required element to load
    await page.waitForSelector(".prayers");

    prayerTimes = await page.evaluate(() => {
      const timeElements = document.querySelectorAll(".prayers .time div");
      const times = Array.from(timeElements).map(
        (element) => element.textContent
      );
      return times;
    });

    console.log("Prayer Times:");
    prayerTimes.forEach((time, index) => {
      console.log(`Prayer ${index + 1}: ${time}`);
    });

    await browser.close();
  }

  async function checkPrayerTimes() {
    const now = new Date();
    const currentTime = now.toLocaleTimeString("en-US", {
      hour12: false,
      hour: "2-digit",
      minute: "2-digit",
    });

    if (prayerTimes.includes(currentTime)) {
      console.log("Het is tijd!!");
      try {
        await soundPlay.play(path.join(__dirname, "../src/audio/azan5.mp3"), 1);
        console.log(`Audio is playing now!`);
      } catch (error) {
        console.error("Error playing audio:", error);
      }
    } else {
      console.log("Het is nog geen tijd!");
    }
  }

  async function runTask() {
    console.log("Running task...");
    try {
      await scrapePrayerTimes();
      console.log("Task completed.");
      await checkPrayerTimes();
    } catch (error) {
      console.error("Error:", error);
    }
  }

  // Schedule the task to run every minute
  cron.schedule("* * * * *", runTask);
})();
