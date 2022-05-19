const PRAYERNAMES = ["Fajr", "Dhuhr", "'Asr", "Maghrib", "'Ishaa"];

const prayerList = async (currentTimes) => {
  return PRAYERNAMES.map((p, i) => {
    console.log(`${p}: ${currentTimes[i]}`);
  });
};

exports.prayerList = prayerList;
