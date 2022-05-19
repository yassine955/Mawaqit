const axios = require("axios");

const fetchAPI = async () => {
  const currentMonth = new Date().getMonth() + 1;
  const currentDay = new Date().getDate();
  const currentYear = new Date().getFullYear();
  const api = `https://izaachen.de/api/times/${2021}/Niederlande/Leiden%20(S%C3%BCdholland).txt`;

  const { data } = await axios.get(api);

  const currentTimes = data["times"][currentMonth][currentDay];

  let PRAYERTIMES = [];
  Object.keys(currentTimes).map((key, index) => {
    if (index !== 1) PRAYERTIMES.push(currentTimes[key]["t"]);
  });

  return PRAYERTIMES;
};

exports.fetchAPI = fetchAPI;
