/* Create Database nao */
CREATE DATABASE IF NOT EXISTS `nao` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `nao`;

/* Create table answers with columns caseID, primary_keywords, secondary_keywords, answer */
CREATE TABLE IF NOT EXISTS `matching_table` (
  `caseID` INT NOT NULL,
  `primary_keywords` varchar(1000) NOT NULL,
  `secondary_keywords` varchar(1000) NOT NULL,
  `answer` varchar(1000) NOT NULL,
  PRIMARY KEY (`caseID`)
) DEFAULT CHARSET=utf8;

/* Insert data into answers */
INSERT INTO matching_table VALUES
    (1,'studiengang,informieren,studium','wie,und,wo,über,hwr,kenntnis,dual','Es gibt eine Übersicht aller Studiengänge auf der Webseite der HWR Berlin. Außerdem findest du dort alle Bewerbungs- und Zulassungsvoraussetzungen. Bei Fragen zur Studienorientierung und Studienwahl kannst du dich an die Allgemeine Studienberatung wenden. Zu vielen Themen bietet auch der Studierendenservice der HWR Berlin regelmäßig Online-Veranstaltungen an, bei denen du ins Gespräch kommen kannst. Und in unserer Instathek kannst du Studierende der HWR Berlin treffen und Infos aus erster Hand bekommen.'),
	(2,'voraussetzung,gelten,brauchen,bedingung','welch,studiengang,informatik,informatikstudium,mitbringen,studieren,wissen','Du benötigst eine anerkannte Hochschulzugangsberechtigung. Diese wären die allgemeine Hochschulreife, also das Abitur, eine fachgebundene Hochschulreife oder Fachhochschulreife, auch Fachabitur genannt oder eine andere Hochschulzugangsberechtigung. Außerdem solltest du auch Interesse am Fach mitbringen.'),
	(3,'bewerben,studium,studiengang','wie,und,wo,für,an,hwr,informatikstudium','Es gibt unterschiedliche Bewerbungsverfahren. Es hängt von deinem Schulabschluss, Fachsemester und Studienziel ab, auf welchem Weg du dich an der Hochschule für Wirtschaft und Recht Berlin für ein Bachelorstudium bewirbst. Ob es dual, normal, ein Bachelor oder Masterstudium werden soll ist ebenfalls ausschlaggebend. Auf dem Onlineportal der HWR gibt es genauere Infos dazu.'),
	(4,'dual,studiengang,studium,bewerben','wie,für,wo,und,informatikstudium,informatik,an,hwr','Die Bewerbung für duale Studiengänge läuft direkt über die Partnerunternehmen der jeweiligen Studiengänge an der HWR Berlin. Bitte beachte: Bei vielen Partnerunternehmen solltest du dich ein Jahr vor Studienbeginn bewerben. Auf der Webseite der HWR findest du auch eine Liste mit allen Partnerunternehmen für jeden Studiengang. Bei weiteren Fragen unterstützt dich auch gerne die Studienberatung.'),
	(5,'dual,aufbau','wie,studium,informatik,informatikstudium,woraus','Das duale Studium der Informatik gliedert sich in den theoretischen und praktischen Teil. In der Praxis werden betriebliche Aufgaben innerhalb des Unternehmens bewältigt. Der theoretische Teil wird an der Hochschule absolviert. In den einzelnen Semestern werden Module wie mathematische Methoden, Betriebssysteme oder Datenbanken behandelt. Neben Klausuren werden auch Praxistransferberichte, Studienarbeiten oder eine Bachelorthesis verfasst.'),
	(6,'bachelor,abschluss,nach','welch,beruf,qualifizieren,was,wofür,machen,studium','Das duale Bachelorstudium qualifiziert sowohl für Tätigkeiten in der Software- Entwicklung als auch in der Systemadministration. Absolventinnen und Absolventen des Studiengangs kommen vor allem in den folgenden Bereichen zum Einsatz: Entwicklungsabteilungen von Unternehmen aus der Softwarebranche, IT-Dienstleister oder unternehmensinterne IT-Abteilungen.'),
	(7,'studiengang','erzählen,informatik,informatikstudium,über,was','Der duale Studiengang Informatik ist einer von derzeit 18 dualen Studiengängen an der HWR. Die Dauer des Studiums beträgt 6 Semester und umfasst mehrere unterschiedliche Module, die Grundwissen und fortgeschrittenes Anwendungswissen vermitteln sollen. Dazu gehören beispielsweise Betriebssysteme, Datenbanken, Software-Engineering, Programmierung und mathematische Module wie Statistik und Datenanalyse. Am Campus Lichtenberg findet der theoretische Teil statt, wobei Probleme und Lösungsmöglichkeiten, spezielle Methoden, kleine Anwendungsbeispiele und theoretisches Wissen vermittelt wird. Der Praxisteil findet im Unternehmen statt und umfasst abteilungsabhängige Aufgaben, die mit dem Theoriewissen einhergehen können.'),
	(8,'studieninhalte,inhalte,studium','was,haben,welch,machen,im,in,dies,dual,enthalten','Das Informatikstudium setzt sich aus Grundlagen wie Mathematik, Programmieren, Software-Engineering und vielen weiteren Modulen zusammen. Dabei werden gesellschaftliche und juristische Aspekte, Problematiken und deren Lösungsansätze sowie grundsätzliches, fachliches Wissen vermittelt und praktisch erläutert.'),
	(9,'ptb','was,bedeuten,vorstellen','Ein Praxistransferbericht, kurz auch PTB genannt, ist eine schriftliche Arbeit, welche während der Praxisphase im Unternehmen geschrieben wird. Der PTB bezieht sich auf ein betriebliches Thema, welches aktuell im Unternehmen anfällt. Diese wissenschaftliche Arbeit geht in die Gesamtbewertung eines Moduls des aktuellen Semesters ein.'),
	(10,'studienarbeit','was,bedeuten,vorstellen','Eine Studienarbeit ist wie ein PTB eine wissenschaftliche Arbeit, bei der von der Hochschule angebotene Themen meistens in kleinen Gruppen, aber auch alleine bearbeitet werden. Der Umfang der Arbeit ist etwa doppelt so groß wie bei einem PTB und diese wissenschaftliche Arbeit geht ebenfalls in die Gesamtbewertung eines Moduls des aktuellen Semesters ein.'),
	(11,'bachelorarbeit','was,bedeuten,vorstellen','Eine Bachelorarbeit ist die Abschlussarbeit eines Bachelor-Studiums und wird sowohl schriftlich verfasst als auch vor einem Publikum präsentiert. Die Präsentation wird auch Kolloquium genannt. Der schriftliche Umfang beträgt etwa das dreifache eines Praxistransferberichts. Diese wissenschaftliche Arbeit geht in die Gesamtbewertung des Studiums ein.'),
	(12,'viel,schreiben,oft','wie,ptb,studienarbeit,studium,während','Im Verlaufe des Studiums werden drei PTBs in den ersten drei Semestern und zwei Studienarbeiten im vierten und fünften Semester geschrieben. Abhängig vom Studiengang kann anstelle der Studienarbeit im fünften Semester eine mündlichge Trasnferprüfung abgehalten werden. Im sechsten Semester wird dann eine Bachelorthesis als Abschlussarbeit verfasst.'),
	(13,'modul,haben','welch,studium,existieren,was,für','Das Informatikstudium besteht aus folgenden Modulen. Die Grundlagen bestehen aus Mathematik, Programmieren, technische Grundlagen der Informatik und theoretischer Informatik. Die übergreifenden Inhalte sind Betriebswirtschaftslehre, Gesellschaftliche und juristische Aspekte der Informatik, Projektmanagement, Softwareengineering, Betriebssysteme, Datenbanken und Netzwerke. Als Wahlpflichtfächer kann man zwischen Grafik und Multimedia, Kommunikationssysteme, Mobile Systeme und Künstliche Intelligenz.'),
	(14,'erzählen,hwr,wissen','über,was','Die Hochschule für Wirtschaft und Recht ist neben der HTW und der Beuth Hochschule eine der größten Hochschulen in Berlin. Sie vereint viele Ausrichtungen und Fachbereiche in einer Hochschule. Ich kann dir gerne etwas mehr über die HWR erzählen. Du kannst mich zum Beispiel nach der Gründung, der Anzahl an Studierenden oder den Standorten fragen.'),
	(15,'wann,gründen,jahr,lang','hwr,öffnen,haben,seit,viel','Die HWR, so wie sie heute bekannt ist, gibt es seit 2009. Sie hat sich aus dem Zusammenschluss der Berlin School of Economics und der Fachhochschule für Verwaltung und Rechtspflege Berlin ergeben.'),
	(16,'viel,student','wie,an,hwr,studieren','An der HWR studieren zurzeit circa 11400 Menschen, wovon über 2000 ein duales Studium machen.'),
	(17,'standort,wo,viel','welch,hwr,wie,haben,überall','Die Hochschule für Wirtschaft und Recht hat 2 Standorte. Diese liegen in Lichtenberg und in Schöneberg. Der Campus Schöneberg und der Standort an der Möckernbrücke werden vom Fachbereich 1 genutzt, während der Campus Lichtenberg von den anderen Fachbereichen verwendet wird.'),
	(18,'viel,fachbereich','wie,hwr,welch,haben,an,was,für,existieren','Die HWR hat 5 Fachbereiche. Diese sind Fachbereich 1 für Wirtschaftswissenschaften, Fachbereich 2 für duales Studium, Fachbereich 3 für Allgemeine Verwaltung, Fachbereich 4 für Rechtspflege und Fachbereich 5 für Polizei und Sicherheitsmanagement.'),
	(19,'viel,studiengang','wie,haben,an,hwr,existieren','Es gibt zurzeit 56 Studiengänge, welche in Bachelor, Master, Fernstudium, duales Studium und berufsbegleitendes Studium unterteilt werden. Davon sind 18 duale Studiengänge.'),
	(20,'welch,studiengang,was','haben,an,hwr,für,bieten,existieren','Die Studiengänge kann man grob in technische und wirtschaftliche Studiengänge unterteilen. Zu den technischen Studiengängen gehören unter anderem Bau-ingenieurwesen, Informatik und industrielle Elektrotechnik. Im Wirtschaftsbereich gibt es zum Beispiel BWL-Industrie und Wirtschaftsinformatik.'),
	(21,'dauern,lang,jahr','wie,studium,gehen,viel,studieren,informatikstudium,informatik','Ein Bachelorstudium hat eine Länge von 6 Semestern und dauert damit circa 3 Jahre lang. Wenn du an dein Bachelorstudium noch einen Master anhängen möchtest, verlängert sich dein Studium um 2 bis 4 Semester.'),
	(22,'informatik,erzählen','über,was,machen,in','Informatik ist die Wissenschaft von der systematischen Darstellung, Speicherung, Verarbeitung und Übertragung von Informationen, besonders der automatischen Verarbeitung mit Digitalrechnern. Historisch hat sich die Informatik einerseits aus der Mathematik als Strukturwissenschaft entwickelt, andererseits als Ingenieursdisziplin aus dem praktischen Bedarf nach der schnellen und insbesondere automatischen Ausführung von Berechnungen.'),
	(23,'heißen,name','wie,was,lauten,wer,nennen','Mein Name ist NAO. Ich bin ein humanoider Roboter.'),
	(24,'woher','kommen,wo,werden,gebären,herstellen,erzeugen,bauen','Ich wurde im Firmenhauptsitz von Softbank-Robotics in Paris entwickelt.'),
	(25,'können,fähigkeit','was,machen,hier','Ich kann alles, was bei mir einprogrammiert wurde. Ich kann mich mit dir unterhalten und ich kann Dinge erkennen und sogar tanzen. Heute habe ich da aber keine Lust darauf und unterhalte mich lieber nur.');

/* Create table generic_terms with columns id, generic_term */
CREATE TABLE generic_terms (
    id INT NOT NULL AUTO_INCREMENT,
    generic_term VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET=utf8;

/* Insert data into generic_terms */
INSERT INTO generic_terms VALUES
    (1,'brauchen'),
	(2,'studiengang'),
	(3,'hwr'),
	(4,'ptb'),
	(5,'schreiben'),
	(6,'studienarbeit'),
	(7,'informieren'),
	(8,'aufbau'),
	(9,'bachelor'),
	(10,'beruf'),
	(11,'bachelorarbeit'),
	(12,'modul'),
	(13,'erzählen'),
	(14,'gründen'),
	(15,'student'),
	(16,'haben'),
	(17,'bewerben'),
	(18,'informatikstudium');


/* Create table synonyms with columns synonym, id */
CREATE TABLE synonyms (
    synonym VARCHAR(255) NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY (synonym, id)
) DEFAULT CHARSET=utf8;

/* Insert data into synonyms */
INSERT INTO synonyms VALUES
    ('brauchen',1),
	('brauche',1),
	('brauch',1),
	('bräuchte',1),
	(' benötigen',1),
	('studiengang',2),
	('studiengänge',2),
	('hwr',3),
	('uni',3),
	('campus',3),
	('universität',3),
	('hochschule',3),
	('ptb',4),
	('praxistransferbericht',4),
	('praxistransferberichte',4),
	('ptbs',4),
	('schreiben',5),
	('verfassen',5),
	('studienarbeit',6),
	('studienarbeiten',6),
	('informieren',7),
	('erkundigen',7),
	('schlaumachen',7),
	('information',7),
	('aufbau',8),
	('aufbauen',8),
	('zusammensetzen',8),
	('zusammensetzung',8),
	('strukturieren',8),
	('struktur',8),
	('bestehen',8),
	('besteht',8),
	('ablaufen',8),
	('laufen',8),
	('bachelor',9),
	('bachelorabschluss',9),
	('beruf',10),
	('berufe',10),
	('berufsfeld',10),
	('berufsfelder',10),
	('bachelorarbeit',11),
	('bachelorthesis',11),
	('modul',12),
	('fach',12),
	('fächer',12),
	('module',12),
	('sagen',13),
	('sag',13),
	('erzählen',13),
	('erzähl',13),
	('gründung',14),
	('gründen',14),
	('student',15),
	('studenten',15),
	('studentin',15),
	('studierende',15),
	('studierender',15),
	('schüler',15),
	('schülerin',15),
	('person',15),
	('personen',15),
	('haben',16),
	('hat',16),
	('besitzt',16),
	('besitzen',16),
	('vorhanden',16),
	('vertreten',16),
	('geben',16),
	('bewerben',17),
	('bewerbung',17),
	('bewerbe',17),
	('bewirbt',17),
	('informatikstudiengang',18),
	('informatikstudium',18);


/* Create table weights with columns keyword, weight */
CREATE TABLE weights (
	keyword text,
	`weight` float);