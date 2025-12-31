# STARVIS

Hello, my name is Nathaniel, and im going to make an AI ally? Colleaugue? Im not quite sure what it is to me. Like a friend I guess.

STATEMENTS

I am an absolute beginner and have never done anything like this. The closest would be Vex coding and working with Edison bots. As Mark Rober said, I expect many struggles and hardships and I embrace them. (or whatever he said i have no idea) 
My "C" button on my keyboard is kinda broken so there may be many missing "C's" (I have to tilt my keyboard to enter "c" lots but not all the time)
No drawings / Schematics / CADS currently and when i make them they will likely be atrocious
i have no clue what im doing but i know i want to do this
As the time of writing this I joined HackClub 2 hours ago after learning about it in a reel.
I've never used a *real coding language before, and since RaspPi uses Python, this will be very hard. I will probably be using Gemini or another LLM to write code that I can edit. This is meant to be a learning experience, and I find myself learning best when "reverse engineering" things
*I've never coded not using blocks but I use scratch alot and I would never forget my day one like that Scratch my goat for real
THIS IS A HUGE PROJECT FOR A BEGINNER LIKE ME I KNOW BUT IT MUST BE DONE
Apologies if this README seems unorganized, as of the time im writing this ive litteraly been on github for a grand total of 1 and a half hours
STARVIS is the project name. The AI's name is TARVIS, so when speaking to it, I call it TARVIS. It just feels better and rolls off the tounge better for me.
Google Gemini was my best friend in this from ideas to naming to everything so thanks Gemini
Its the next day and i realized TARVIS is close to TARDIS so it might end up looking like that

UNCONFIRMED / LATER ADDITIONS

2 knobs, one for personality changing (JARVIS to TARS) and one for more specfic personality traits like TARS's humour and honesty sliders


DESCRIPTION / PLAN

Repository for my desktop AI friend/assistant/companion using a Raspberry Pi 5 16GB (hopefully) or 8GB running Ollama for basic conversing, DeepSeek R1 (I think thats the right model, the local one anyway) for "smarter" responses, and Gemini API for the real brains. 
I have been planning vigorously, using Google Gemini to help me. The goal is to have a (almost) fully private, smart, expressive local LLM AI to chat with while im on my PC, whether it be discussing game stratigies or bored and wanting something to do. 
If you (the reader) has an Alexa, or a Google Home, etc. Its meant to be like that and a mix of Gemini Live, combining genius with functionality,
Its designed to be able to do many things, (if marked with ">" i will go into more detail as some things are annoying to explain or speak for themselves) such as 
>local LLM processing, >PC headset integration, >custom personalities, voice-activation, >"tactical" HUD, >headset-on detection, "vision" system, >"huddle" button, and a >visual status indicator. (lots i know)

(Not so) DETAILED EXPLANATIONS

Local LLM Processing
Speaks for itself.
A local AI hosted on the RaspPi for privacy.

PC Headset Integration
STARVIS will act as an inbetween for audio and mic between the headset and my PC.
This allows for the "huddle button" which I'll get into later.

Custom Personalities
So I can make them like their characters. (TARS/JARVIS)
I plan to have a personality ratio of J30:T70, this means it will be 70% like TARS with his humour and wits and 30% JARVIS with his "butlerism" and judginess / passive aggressiveness

"Tactical" HUD
Just a Pi 5 screen with some analytics on it probably of PC / Pi performances / temps 
I want STARVIS to be able to cycle between things based off of context, like if i ask "hey TARVIS whats the weather?"

"Huddle" button
One of the ideas i came up with.
When you press and hold the button, it cuts mic audio from the Pi to the PC so when you speak, its solely to TARVIS.
*press and hold button* "hey TARVIS this guy reading this is cool right"
"yeah this reader is hella cool" and the people on discord would have no clue


Why?

Recently, I've been in the "wow theres no fun games anymore and I need something to do before I lose my mind from doomscrolling for hours" phase. I thought to myself, I need a project. So I did. 
I made a wheres waldo type game on Google Slides for my friends at school to play while we were bored. But that died out like the 2 week Minecraft phase. There I was again. Staring at my phone like a zombie, when all of the sudden, a reel showing what a Pi-Hole is showed up.
"What is this? Get off my feed, I never placed this brick." I said. And I died of boredom later that day. JOKE!! Im still alive.
What really happened is this; I watched the video. "cool but i already have adblockers." 
Skip ahead few days and i got a youtube recommendation for another Raspberry Pi project. "Wow that looks like fun!" so here i am.


NAMING

STARVIS, (Stationary Tactical Analytic Response & Virtual Intelligence System) is a mix between TARS from the movie Interstellar, and JARVIS from Iron Man, two extremely intelligent artificial intelligences (duh). Im sure you've seen them or heard of them before.
I chose the name STARVIS because i was originally torn between STARS (Stationary TARS) and TARVIS (TARS+JARVIS), so I thought, why not STARVIS? Best out of both worlds. And it sound like TARDIS so i could design it like that


SHOPPING LIST / BOM
**EVERYTHING IS IN CAD**

Brain + Power -	[CanaKit Pi 5 (16GB) Turbine Kit (Case, PSU, 128GB SD)](https://www.canakit.com/canakit-raspberry-pi-5-starter-kit-turbine-black.html?defpid=5062)	$229.95
The HUD -	[8.8" Bar LCD (Amazon.ca)](https://www.amazon.ca/Touchscreen-Stretched-Portable-Raspberry-Monitoring/dp/B0F6L7ZB2T/ref=sr_1_5?dib=eyJ2IjoiMSJ9.3_gx_1CPfnXGbBpAiDIi6Vr0j1gu60DBMbTzN2RfH_rdvBFVylB3cZSZWRJ8FgPpZ8ODs-un6BjbaKwl_WaIaoJYSvcb0TvnNz4mKpKmvIzRAS_EzXDKOkMU55N2lQClZ3qUL7DJ-p5fiOJho6233Dr3LxXZ8aAgwK0MV5Gr5Wypfy06Ma6fTNwxwhuqRfTkXhZhvZT4SbIvjs268DIAPrj93dY-Ruls8IlaEBgPxGT07O3_WsTtYmbsPOrT0vDJCEB5TY1FpmksMpyvuhZCkk-yda--prkWbma1VuPEc04.K1wQV6fSchMNak41wTZsEofPTqTobVoRlSB75H__Hr8&dib_tag=se&keywords=8.8+inch+raspberry+pi+display&qid=1767193344&sr=8-5)	$69.99 
M.2 Interface -	[Raspberry Pi M.2 HAT+ (PiShop](https://www.pishop.ca/product/raspberry-pi-m-2-hat-for-pi-5/)	$16.95
SSD Storage -	[500GB NVMe SSD (Amazon.ca)](https://www.amazon.ca/XPG-GAMMIX-S55-High-Performance-SGAMMIXS55-512G-C/dp/B0FH5PH5P7/ref=sr_1_5?crid=2LEGMRLIDFKKW&dib=eyJ2IjoiMSJ9.vVHAUJcMMkHk2B0Ax9o8KFhdVK-vizSZoqko2qpM6uFX8HaZ67sT9TatoaIfEebQCZrrnZOWyCOWZ-xkqpRUKetM5lK-nEdY50fwSg4Cj70i2Wy8hwOe8khGvuhNJPjnkSeyAl10ZN4_a7oCE7ZiWkex3hBTUdlbh4cse3ZoMHCXR6XUBGVNG9jWLFYuR3FhbPhCxdtFhHQsckM24XMvU7UgFZQxQ83CynCI47KPNYXCMXla8SKIZUkPjzNE2rZZ6lEQbmo6Af7MJxJAiYsU0890izQktpbzxowtP7xKwko.d_50WXWs0Q35ZYK3pCyizr4pmzbus0tlnPbYdaou0uA&dib_tag=se&keywords=nvme+2230&qid=1767194148&refinements=p_36%3A-7600&rnid=12035759011&sprefix=nvme+2230%2Caps%2C112&sr=8-5)	$74.99 **ONE LEFT IN STOCK**
Audio Adapter	- [USB Audio DAC (PiShop)](https://www.pishop.ca/product/usb-audio-adapter-works-with-raspberry-pi/)	$6.95
Camera Module	- [Pi Camera Module 3 (PiShop)](https://www.pishop.ca/product/raspberry-pi-camera-module-3/)	$36.45
Huddle Button -	[16mm LED Button (Amazon.ca)](https://www.amazon.ca/DMWD-Indicator-Waterproof-Self-Locking-Pre-Wired/dp/B09HS9KW9T/ref=sr_1_8?crid=149RP2D322B2P&dib=eyJ2IjoiMSJ9.8L87-rgZSu7XidE-F-zNaXxbKRkdyb4Q3paLBAP7LVmimkYwdNuaUo3BuNsJCwP-xxdYppSofOF85unllv48iletj0MOsNNnAmtu9FV4tY-hpZ-kWyPHfYOk5U7S4FPjELrZ_tXcmHAV2i2hGY46pPt5cVnDHpY3si2eoUXJY88kIUN_jmE9U5_Jbe9pBZVnFIqM3Sv5Lu45L1LdgLR2ZlMMw7WBafmHtB2iA9tpt-6-P9qY8VfrptK_IqZ5dA29lFsm0UojNJXRm0nDWYmL2654wMHIL3TLs-OaNApPt4s.fWfNYkMP9MQAAv0NCeA9c1NaGWEQtTAcOuU_R-uMgRE&dib_tag=se&keywords=16%2Binch%2Bbutton%2BLED%2Belectronic&qid=1767194311&sprefix=16%2Binch%2Bbutton%2Bled%2Belectronic%2Caps%2C100&sr=8-8&th=1)	$19.49
---	---	---
SUBTOTAL (CAD)	$454.77 TAX + SHIPPING NOT INCLUDED
ROUGH TAX ESTIMATE (NOVA SCOTIA 15% HST) ~$70
ROUGH TOTAL ~$530
GRANT (~$540 CAD) (~$395 USD)

