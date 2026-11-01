const crowd = document.getElementById('crowd-grid');
const people = document.createDocumentFragment();
for (let index = 0; index < 100; index += 1) {
  const person = document.createElement('span');
  person.className = `crowd-person ${index < 34 ? 'kid' : index < 71 ? 'teen' : 'adult'}`;
  person.setAttribute('aria-hidden', 'true');
  people.append(person);
}
crowd.append(people);

document.getElementById('print').addEventListener('click', () => window.print());

const rooms = [...document.querySelectorAll('.corridor li')];
const roomDescriptions = [
  'a friend invites. Keyholder: the friend.',
  'we choose a horror game. Keyholders: the friend, on Roblox’s surfaces.',
  'we get into the same server. Keyholder: Roblox.',
  'learning feels easy. Keyholder: the creator.',
  'we laugh together. Keyholder: the group.',
  'a possible return, not yet observed. Keyholders: Roblox and creators.',
];
let currentRoom = 0;
document.getElementById('journey-next').addEventListener('click', () => {
  rooms[currentRoom].classList.remove('is-current');
  rooms[currentRoom].removeAttribute('aria-current');
  currentRoom = (currentRoom + 1) % rooms.length;
  rooms[currentRoom].classList.add('is-current');
  rooms[currentRoom].setAttribute('aria-current', 'step');
  document.getElementById('journey-status').textContent =
    `Room ${currentRoom + 1} of ${rooms.length}: ${roomDescriptions[currentRoom]}`;
});

const maze = document.querySelector('.maze-wrap');
const browseButton = document.getElementById('route-browse');
const friendButton = document.getElementById('route-friend');
function selectRoute(withFriend) {
  maze.classList.toggle('friend-selected', withFriend);
  friendButton.setAttribute('aria-pressed', String(withFriend));
  browseButton.setAttribute('aria-pressed', String(!withFriend));
  document.getElementById('route-status').textContent = withFriend
    ? 'With a friend: one sentence answers the group’s questions before the click.'
    : 'On your own: four questions the game page leaves open.';
}
browseButton.addEventListener('click', () => selectRoute(false));
friendButton.addEventListener('click', () => selectRoute(true));

const balanceButton = document.getElementById('balance-toggle');
balanceButton.addEventListener('click', () => {
  const longTerm = balanceButton.getAttribute('aria-pressed') !== 'true';
  document.querySelector('.balance-stage').classList.toggle('long-term', longTerm);
  balanceButton.setAttribute('aria-pressed', String(longTerm));
  balanceButton.textContent = longTerm ? 'Show the two priorities' : 'See the Q2 bet';
  document.getElementById('balance-status').textContent = longTerm
    ? 'Q2: recommendations tipped toward games people return to. Q3: Roblox reports retention and monetization improved.'
    : 'Two priorities. The illustration has no financial scale.';
});

const guidanceToggle = document.getElementById('guidance-toggle');
guidanceToggle.addEventListener('change', () => {
  document.getElementById('guidance').textContent = guidanceToggle.checked
    ? 'Example only: yes, no guide needed.'
    : 'Not provided by the creator.';
  document.getElementById('state-message').textContent = guidanceToggle.checked
    ? 'Fictional guidance, clearly labeled as creator-provided.'
    : 'Missing information stays visibly missing.';
});

function revealLinkedNotes() {
  const target = document.getElementById(window.location.hash.slice(1));
  if (target instanceof HTMLDetailsElement) target.open = true;
}
window.addEventListener('hashchange', revealLinkedNotes);
revealLinkedNotes();

const videos = {
  hunt: {
    id: 'I7pmbho1DUQ',
    title: 'The Hunt: Mega Edition — official Roblox trailer',
  },
  discovery: {
    id: 'K7jsk3bzmvE',
    title: 'How the Recommended for You algorithm works — Roblox Creators',
  },
};

document.querySelectorAll('[data-load-video]').forEach((button) => {
  button.addEventListener('click', () => {
    const video = videos[button.dataset.loadVideo];
    const shell = button.closest('.video-shell');
    const stage = shell.querySelector('.video-stage');
    const iframe = document.createElement('iframe');
    iframe.title = video.title;
    iframe.src = `https://www.youtube-nocookie.com/embed/${video.id}`;
    iframe.allow = 'encrypted-media; picture-in-picture; fullscreen';
    iframe.allowFullscreen = true;
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    stage.replaceChildren(iframe);
    shell.querySelector('.video-status').textContent =
      'Player requested from YouTube. If playback is blocked or unavailable, use the original-source link alongside it.';
    iframe.focus();
  });
});
