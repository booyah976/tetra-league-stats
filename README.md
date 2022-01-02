<h1>Tetra League Stats</h1>
Gets and stores tetra league game stats (score, APM, PPS, VS) from downloaded replay files


<br>
<h2>Installation</h2>
<ul>
<li>Download/Clone the repository
<li>Create a folder called <code>replays</code> within the current repository if it doesnt already exist
</ul>

<h2>Usage</h2>
<ul>
<li>After a Tetra League game, download your replay to <code>replays</code>
<li>Run <code>main.py</code>
    <ul>
    <li>Stores the game stats from the replays folder without adding comments by default
    <li>-r / --run:
    <ul>
    <li>-r c : prompts to add comments for every replay
    <li>-r nc : dont add comments for any replay
    <li>-r csv : opens <code>data.csv</code>
    </ul>
    </ul>

<li>Data is stored as a csv in <code>data.csv</code>
<li>Have a mental break down because you havent improved in 6 months
<li>Optionally create a <code>saved_replays</code> folder to stockpile on replays as the <code>replays</code> folder is purged every time the program is run. The program automatically moves the replays to said folder after running.