function simpleMovingAverage(prices, window = 24) {
  if (!prices || prices.length < window) {
    return [];
  }

  let index = window - 1;
  const length = prices.length + 1;

  const simpleMovingAverages = [];

  while (++index < length) {
    const windowSlice = prices.slice(index - window, index);
    const sum = windowSlice.reduce((prev, curr) => prev + curr, 0);
    simpleMovingAverages.push(sum / window);
  }

  return simpleMovingAverages;
}