# VIDEO7 Studio — no viena klipa līdz gatavam video

**Piemērs.** [Atver VIDEO7 studiju](https://areteaios.com/lv/my/video-demo) un pirmajā testā noskaties ierakstu pirms un pēc montāžas. Abos ir tās pašas piecas sekundes ar Egila īsto balsi. Otrajā video grafika renderēta ar Chromium un uzlikta ierakstam ar FFmpeg. Angļu un latviešu subtitri ir atsevišķi WebVTT celiņi. [Video Studio in English](https://areteaios.com/my/video-demo).

**Ko uztaisīsi pats.** No viena īsta klipa izveidosi īsu salīdzinājumu pirms un pēc montāžas, skaidru virsrakstu kadrā un rediģējamus subtitrus. Zemāk parādīta vienkārša lokāla versija ar FFmpeg. Pilnajā demo grafikai ir vairāk slāņu un tiek lietots Chromium.

## Ātrais sākums

1. Paņem vienu savu runas klipu. Izvēlies vienu domu, auditoriju, vēlamo garumu un vietu, kur video skatīsies. Izmēģinājumam pietiek ar piecām sekundēm no jau samontēta vai labi saprotama klipa.
2. Atver klipu un atrodi teikuma sākumu un beigas. Atstāj īsu pauzi abās pusēs. Pieraksti, no kura brīža līdz kuram griezīsi, un izvēlies vietu vienam virsrakstam, kas neaizsedz seju.
3. Saglabā pārskatāmu sākuma versiju. Izveido otru no tieši tā paša fragmenta, pievieno nosaukumu un saglabā sākotnējo runu. Ja lieto video redaktoru, atstāj sākuma un montēto versiju atsevišķās laika līnijās vai versijās.
4. Pārlasi runas atšifrējumu oriģinālvalodā un izlabo kļūdas. Ja vajag tulkojumu, izveido otru subtitru failu ar tiem pašiem laika kodiem. Laika kodus skaita no eksportētā fragmenta sākuma.
5. Salīdzini abus MP4 telefonā ar skaņu un subtitriem. Pārbaudi pirmo un pēdējo vārdu, seju un oriģinālo balsi, subtitru salasāmību un grafikas novietojumu.

**Nokopē savam AI**

> Izmanto VIDEO7 un šo praktisko studijas rokasgrāmatu. No viena mana runas klipa izveido divas versijas ar vienu un to pašu fragmentu. Pirmā versija ir tīra, otrajā pievieno virsrakstu vai grafiku un saglabā manu balsi. Pajautā auditoriju, garumu un vajadzīgo subtitru valodu, ja tas vēl nav zināms. Vispirms parādi griezuma laiku, virsrakstu un subtitru tekstu. Saglabā oriģinālu neskartu. Sagatavo divus MP4, rediģējamu subtitru failu un īsu pārbaudes pierakstu. Strādā lokāli un atstāj rezultātu manai apskatei.

Ja čats nevar atvērt lokālus failus vai darbināt video rīkus, palūdz tam sagatavot montāžas plānu un komandas no paša iesniegtas transkripcijas vai laika kodiem. Montēt vai renderēt var redaktorā vai aģentā, kam dota piekļuve konkrētajiem failiem un rīkiem.

## Lokāls montāžas piemērs ar FFmpeg

Šis piemērs paredzēts parastam SDR MP4 ar vienu video un vienu izvēles audio celiņu. Tam vajag FFmpeg ar `libx264` un `drawtext`, kā arī datorā reģistrētu fontu ar vajadzīgajām rakstzīmēm. Pārbaudi ar `ffmpeg -hide_banner -filters`. HDR materiālam, mobilā video mainīgam kadru ātrumam un precīzai griezuma sinhronizācijai izmanto [pamata VIDEO7 norādes](https://github.com/arete-aios/aios/blob/main/skills/video7/SKILL.md) un [montāžas metodi](https://github.com/arete-aios/aios/blob/main/skills/video7/references/cutting-code.md).

Atver projekta mapi, liec klipa kopiju `sources/clip.mp4` un pārbaudi tās ilgumu, attēlu un skaņu. Šeit 0.00 ir izmēģinājuma sākums un 5.00 ir tā ilgums sekundēs. Aizstāj abus ar pārbaudītu fragmentu.

```sh
mkdir -p work out
ffprobe -v error -show_format -show_streams -of json sources/clip.mp4 > work/source-clip.json
printf '%s\n' 'Mana ideja piecās sekundēs' > work/title.txt

ffmpeg -n -ss 0.00 -i sources/clip.mp4 -t 5.00 \
  -map 0:v:0 -map '0:a:0?' -map_metadata -1 -map_chapters -1 \
  -vf 'pad=ceil(iw/2)*2:ceil(ih/2)*2' \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 160k \
  -movflags +faststart out/before-v01.mp4

ffmpeg -n -i out/before-v01.mp4 -map 0:v:0 -map '0:a:0?' \
  -vf "drawtext=textfile=work/title.txt:expansion=none:fontcolor=white:fontsize=h*0.044:x=w*0.06:y=h*0.08:box=1:boxcolor=0x0A121F@0.84:boxborderw=10" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy \
  -movflags +faststart out/edited-v01.mp4
```

Ja uzraksts kadrā nesatilpst, saīsini tekstu vai samazini fontu un saglabā versiju ar citu numuru. Ja `drawtext` nav pieejams, izmanto video redaktora teksta slāni vai izveido caurspīdīgu PNG ar derīgu fontu. Logo vajadzības gadījumā pievieno no sava zīmola apstiprinātajiem materiāliem. Pirms izveides pārbaudi, cik ilgi tiešām skan izvēlētais teikums un vai tajā ir pietiekama pauze.

### Subtitri abām versijām

Ieraksti tava teikuma tekstu failā `work/captions-lv.srt`. Šis ir formāta paraugs. Aizstāj vārdus un laikus ar tiem, ko dzirdi gala fragmentā.

```srt
1
00:00:00,950 --> 00:00:04,800
Mana ideja piecās sekundēs.
```

Saglabā SRT rediģēšanai un konvertē uz WebVTT tīmekļa atskaņotājam.

```sh
ffmpeg -n -i work/captions-lv.srt out/captions-lv.vtt
```

Tīmeklī to pašu `captions-lv.vtt` pieliec abiem piecu sekunžu MP4 ar `<track kind="captions" src="captions-lv.vtt" srclang="lv" label="Latviešu" default>`. Ja ieraksts ir citā valodā, oriģinālvalodas celiņam lieto `kind="captions"` un tulkojumam `kind="subtitles"` ar attiecīgo `srclang`. Turi VTT un lapu vienā izcelsmē, lai pārlūks var nolasīt celiņu. Ja vēlāk mainās fragments, pārliec un vēlreiz pārbaudi laika kodus. Izvēlētais publicēšanas kanāls var prasīt SRT augšupielādi, citu formātu vai subtitrus pašā attēlā.

### Pārbaudi failus

```sh
for file in out/before-v01.mp4 out/edited-v01.mp4; do
  ffprobe -v error -show_entries format=filename,duration:stream=codec_type,codec_name,width,height \
    -of json "$file"
done
```

- Abi faili atveras un satur to pašu izvēlēto fragmentu. Ja avotā bija audio celiņš, atskaņo abus un pārliecinies par sakritību. Piemērā montētā faila kodētais audio tiek pārkopēts no sākuma versijas.
- Apskati kadru klipa sākumā un beigās. Pārbaudi, vai laika gaitā skaņa neaizkavējas un vai grafika neaizsedz skatienu, seju vai subtitrus.
- Atver subtitru failu reālajā atskaņotājā un pārbaudi katra teikuma laiku, rakstību un maiņu starp valodām. Saglabā avotu un izvadfailu nosaukumus un pieraksti izmantoto renderēšanas metodi.
- Nodod pārskatīšanai MP4, SRT vai VTT, īso griezuma pierakstu un rediģējamu projektu, ja tas prasīts. Publicēšanai vajadzīgā piekrišana, galamērķis un licences tiek saskaņotas atsevišķi.

## Septiņi VIDEO7 studijas uzdevumi

Izvēlies vienu rindu. Ja salīdzini vairākas metodes vai rīkus, saglabā vienu materiālu kopu, vienādu uzdevumu, vajadzīgo rezultātu un vērtēšanas kritērijus. Pieraksti metodi, rīku un modeļa versiju, faktiskos ievades materiālus, laiku un izmaksas. Atzīmē trūkstošus datus un to, ko katrs rīks nav varējis pieņemt. Skaidri pieraksti, kuri kadri ir filmēti, ģenerēti vai programmatiski papildināti.

| Tests | Ievade un mērķis | Ko pārbaudīt |
| --- | --- | --- |
| 1. Īsta ieraksta montāža / Editing real footage | Esošs runātāja klips, skaņa un zīmola faili. Izveido publicēšanai piemērotu montāžu ar titriem un grafiku. | Runātāja balss un seja saglabājas, titri ir salasāmi telefonā. |
| 2. Tas pats vēstījums jaunā vidē / Same message, new setting | Esošs klips un vides apraksts. Uztaisi ievadu vai ievieto īsto runu jaunā vidē. | Runas saturs un ritms saglabājas, pāreja darbojas, vide palīdz vēstījumam. |
| 3. Digitāls runātājs / A digital presenter | Paša attēls, balss atsauce un scenārijs. Izveido skaidrojumu bez jauna filmējuma. | Līdzība, izruna, lūpu sinhronizācija un skaidrs noslēgums. |
| 4. Uzstāšanās konferencē / Presenting on a conference stage | Runātāja atsauce, skatuves apraksts un uzaicinājuma teksts. Izveido platāku ainu. | Ticams mērogs un kustības, skaidri saprotama runa. |
| 5. Mārketings ar darbību / Marketing in motion | Produkta stāsts, vizuālā atsauce un viena doma. Parādi ieguvumu īsā ainā ar darbību. | Skatītājs var nosaukt ieguvumu, darbība to pastiprina. |
| 6. Biznesa idejas skaidrojums / A business explainer | Viens biznesa jautājums, procesa soļi un īss stāstījums. Parādi, kā informācija kļūst par izmantojamu rezultātu. | Skatītājs var izsekot soļiem un saprot rezultātu. |
| 7. Personīgs mūzikas klips / A personal music clip | Paša foto, balss atsauce un muzikāla ideja. Izveido īsu dziedāšanas un kustības skici. | Kustība atbilst ritmam, balss skaidra, izmantoto materiālu tiesības ir dokumentētas. |

Filmētam skaidrojumam sāc ar pirmo testu. Sestais noder, ja vērtību vieglāk parādīt ar shēmu vai animāciju. Personīgai balsij un identitātei izmanto savus materiālus vai dokumentētu piekrišanu.

## English quick start

1. [Play the public before/after example](https://areteaios.com/my/video-demo). It uses the same five seconds of Egils’s footage and original voice. The edited clip adds graphics rendered with Chromium and composited with FFmpeg.
2. Pick one line from your own recording and keep some room tone before and after it. Export the same span twice. Add one short headline to the second version. Keep the original file and keep the source voice in the edit.
3. Time an editable SRT against the exported clip and convert it to WebVTT for the browser. Add a separate translated track if needed. The commands above create the paired versions and inspect the resulting files. Replace the supplied headline and cue with your own text.
4. Check the two files on a phone with sound and captions. Record the source file, selected span, overlay method, output versions and any issues. Keep the MP4s and subtitle file together.

**Prompt to copy**

> Use VIDEO7 and this Studio guide. Make a before/after edit from the same span in one of my recordings. Plan the cut, on-screen title and captions first. Keep my source and original voice. Give me two local MP4s, editable captions and a short verification note. Ask me about the audience, destination, length or language only where it matters. Use a local workflow and leave the files ready for my review.

Technical references: [FFmpeg filters and overlays](https://ffmpeg.org/ffmpeg-filters.html), [ffprobe](https://ffmpeg.org/ffprobe.html), [WebVTT](https://www.w3.org/TR/webvtt1/) and [the HTML track element](https://html.spec.whatwg.org/multipage/media.html#the-track-element).
