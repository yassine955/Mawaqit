import { PRAYERNAMES } from "../config";

export const prayerList = async (currentTimes: string[]) => {
  return PRAYERNAMES.map((p, i) => {
    console.log(`${p}: ${currentTimes[i]}`);
  });
};
