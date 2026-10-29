const crowd = document.getElementById('crowd-grid');
const people = document.createDocumentFragment();
for (let index = 0; index < 100; index += 1) {
  const person = document.createElement('span');
  person.className = `crowd-person ${index < 35 ? 'kid' : index < 73 ? 'teen' : 'adult'}`;
  person.setAttribute('aria-hidden', 'true');
  people.append(person);
}
crowd.append(people);

document.getElementById('print').addEventListener('click', () => window.print());

const rooms = [...document.querySelectorAll('.corridor li')];
const roomDescriptions = [
  'a friend invites.',
  'we choose a horror experience.',
  'we enter the game.',
  'learning feels easy in this session.',
  'we have fun together.',
  'a possible return, not a reported visit.',
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
    ? 'Friend-led: someone gives you a starting point. The shorter line is a metaphor, not a speed claim.'
    : 'Browsing: the platform helps you explore. This is a metaphor, not measured click distance.';
}
browseButton.addEventListener('click', () => selectRoute(false));
friendButton.addEventListener('click', () => selectRoute(true));

const balanceButton = document.getElementById('balance-toggle');
balanceButton.addEventListener('click', () => {
  const longTerm = balanceButton.getAttribute('aria-pressed') !== 'true';
  document.querySelector('.balance-stage').classList.toggle('long-term', longTerm);
  balanceButton.setAttribute('aria-pressed', String(longTerm));
  balanceButton.textContent = longTerm ? 'Show the two priorities' : 'See the long-term bet';
  document.getElementById('balance-status').textContent = longTerm
    ? 'The reported bet: favor long-term retention, accepting a near-term monetization impact. Not a forecast.'
    : 'Two priorities. The illustration has no financial scale.';
});

const guidanceToggle = document.getElementById('guidance-toggle');
guidanceToggle.addEventListener('change', () => {
  document.getElementById('guidance').textContent = guidanceToggle.checked
    ? 'Example only: choose a lobby before starting a round.'
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
