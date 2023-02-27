export const parseStampTime = (stamp) => {
  const D = new Date(stamp);
  return `${D.getFullYear()}/${D.getMonth()}/${D.getDay()} ${D.getHours()}:${D.getMinutes()}`;
};
