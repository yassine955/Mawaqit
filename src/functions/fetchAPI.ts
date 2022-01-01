import axios from "axios";

export const fetchAPI = async () => {
  const currentMonth: number = new Date().getMonth() + 1;
  const currentDay: number = new Date().getDate();
  const currentYear: number = new Date().getFullYear();
  const api: string = `https://izaachen.de/api/times/${2021}/Niederlande/Leiden%20(S%C3%BCdholland).txt`;

  const { data } = await axios.get(api);

  const currentTimes = data["times"][currentMonth][currentDay];

  let PRAYERTIMES: string[] = [];
  Object.keys(currentTimes).map((key, index) => {
    if (index !== 1) PRAYERTIMES.push(currentTimes[key]["t"]);
  });

  return PRAYERTIMES;
};
