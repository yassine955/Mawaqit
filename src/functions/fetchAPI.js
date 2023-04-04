const axios = require("axios");
const cheerio = require("cheerio");

const fetchAPI = async () => {
  const cookie = "currentCity=29263; Domain=www.al-yaqeen.com; Path=/";

  const res = await axios.get("https://www.al-yaqeen.com/gebedstijden/", {
    headers: {
      Cookie: cookie,
    },
  });

  const $ = cheerio.load(res.data);
  const prayers = [];

  $("tr.prayer-table__day.current td").each((i, el) => {
    const time = $(el).text().trim();

    prayers.push(time);
  });

  prayers.splice(1, 1);

  return prayers;
};

exports.fetchAPI = fetchAPI;
