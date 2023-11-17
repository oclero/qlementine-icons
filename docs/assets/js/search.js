'use strict';

const MIN_SEARCH_TEXT_LENGTH = 2;

const IGNORED_WORDS = ['a', 'an', 'the'];

const INDEX_URL = BASE_URL + 'index.json';

let fetchedList = null;
let searchText = '';
let searchboxNode = null;
let listNode = null;
let noResultsNode = null;

function fetchJsonIndex(url, onDataReceived) {
  const startTime = performance.now();
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      console.info(
        `JSON index fetched at ${url} in ${(performance.now() - startTime).toFixed(2)}ms.`,
      );
      onDataReceived(data.data);
    })
    .catch((error) => {
      console.error(`Failed to fetch JSON index at ${url}: ${error.message}`);
      onDataReceived({});
    });
}

function ensureIndexFetched() {
  if (fetchedList !== null) return;

  fetchJsonIndex(INDEX_URL, (data) => {
    if (data && data.hasOwnProperty('icons')) {
      const normalizedList = data.icons.map((item) => {
        return {
          name: item.name,
          normalizedName: normalizeString(item.name),
          path: item.path,
          freedesktop: item.freedesktop,
          tags: item.tags,
        };
      });
      fetchedList = normalizedList;

      if (searchText.length > MIN_SEARCH_TEXT_LENGTH) {
        triggerSearch();
      }
    } else {
      fetchedList = null;
      searchText = '';
    }
  });
}

function triggerSearch() {
  if (fetchedList == null || fetchedList.length == 0) return;

  const matchingItems = getSearchResult(searchText, fetchedList);
  updateList(matchingItems);
}

function updateList(matchingItems) {
  if (matchingItems.length > 0) {
    noResultsNode.style.display = 'none';
  } else {
    noResultsNode.style.display = 'block';
  }

  // Hide/show list elements based on the result.
  const listElements = listNode.getElementsByTagName('tr');
  for (const listElement of listElements) {
    const listElementName = listElement.dataset.name;
    const found = matchingItems.find((item) => {
      return item.name === listElementName;
    });
    listElement.style.display = found ? 'table-row' : 'none';
  }
}

function normalizeString(query) {
  let normalizedQuery = query.trim();
  normalizedQuery = normalizedQuery.replace(/[^\w\s]|_/g, ' ').replace(/\s+/g, ' ');
  normalizedQuery = normalizedQuery.toLowerCase();
  return normalizedQuery;
}

function getQueryTokens(query) {
  return query
    .split(' ')
    .filter((word) => !IGNORED_WORDS.includes(word) && word.length >= MIN_SEARCH_TEXT_LENGTH);
}

// TODO
// Check item.freedesktop
function getScore(query, tokens, item) {
  let score = 0;

  // Check if name contains the whole query.
  if (item.normalizedName.includes(query)) score += 100;

  // Check if each word of the query is in name or tags.
  tokens.forEach((token) => {
    // Check name.
    if (item.normalizedName.includes(token)) score += 3;

    // Check tags.
    item.tags.forEach((tag) => {
      if (tag.includes(token)) score += 1;
    });
  });

  return {
    name: item.name,
    score: score,
  };
}

function filterScore(item) {
  return item.score > 0;
}

function compareScores(item1, item2) {
  // Sort best scores first.
  if (item1.score < item2.score) return 1;
  if (item1.score > item2.score) return -1;
  // Sort same scores alphabetically.
  if (item1.name < item2.name) return -1;
  if (item1.name > item2.name) return 1;
  return 0;
}

function getSearchResult(query, list) {
  if (list === null || list === undefined || !Array.isArray(list) || list.length === 0) return [];

  if (query.length < MIN_SEARCH_TEXT_LENGTH) return list;

  const normalizedQuery = normalizeString(query);
  console.log(`Normalized input: ${normalizedQuery}`);

  const normalizedQueryTokens = getQueryTokens(normalizedQuery);
  const scores = list.map((item) => getScore(normalizedQuery, normalizedQueryTokens, item));
  const matchingScores = scores.filter(filterScore);
  console.log(`Matches: ${matchingScores.length}`);

  const sortedScores = matchingScores.sort(compareScores);
  console.log(sortedScores);

  // Get only the first n items.
  const result = sortedScores.slice(0, 100);

  return result;
}

function triggerFileDownload(fileName, url) {
  const anchor = document.createElement('a');
  anchor.style.display = 'none';
  anchor.href = url;
  anchor.download = fileName;
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
}

function setupTableRows() {
  const rows = listNode.getElementsByTagName('tr');
  for (const row of rows) {
    const cells = row.getElementsByTagName('td');
    const iconCell = cells[0];
    iconCell.addEventListener('click', () => {
      const iconName = `${row.dataset.name}.svg`;
      const iconUrl = BASE_URL + row.dataset.url;
      triggerFileDownload(iconName, iconUrl);
    });
  }
}

function setupSearchField() {
  searchboxNode.addEventListener('focusin', () => {
    ensureIndexFetched();
  });

  searchboxNode.addEventListener('input', () => {
    if (searchboxNode.value != searchText) {
      searchText = searchboxNode.value;
      triggerSearch();
    }
  });
}

document.addEventListener('DOMContentLoaded', function () {
  searchboxNode = document.getElementById('searchbox');
  if (!searchboxNode) return;

  listNode = document.getElementById('list');
  if (!listNode) return;

  noResultsNode = document.getElementById('noresults');
  if (!noResultsNode) return;

  setupSearchField();
  setupTableRows();
});
