export const parseStampTime = (stamp) => {
  const D = new Date(stamp * 1000);
  console.log(D);
  return `${D.getFullYear()}/${D.getMonth()}/${D.getDay()} ${D.getHours()}:${D.getMinutes()}`;
};

export const stampToUTCtime = (stamp) => {
  return new Date(stamp * 1000);
};

export const timeToStamp = (time) => {
  return Date.parse(time.toString()) / 1000;
};
