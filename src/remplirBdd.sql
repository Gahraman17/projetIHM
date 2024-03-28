INSERT INTO
    questions (
        category_id, text, option1, option2, option3, correct_option, explication
    )
VALUES (
        1, 'livre écrit par un auteur russe', 'A. Crime et Châtiment', 'B. Anna Karénine', 'C. Les Misérables', 3, 'Les Misérables est une œuvre de Victor Hugo, un écrivain français.'
    ),
    (
        1, 'œuvre appartenant au courant existentialiste', 'A. L''Étranger', 'B. La Nausée', 'C. Le Comte de Monte-Cristo', 3, 'Le Comte de Monte-Cristo est un roman d''aventure écrit par Alexandre Dumas.'
    ),
    (
        1, 'écrivain associé au théâtre', 'A. Molière', 'B. Shakespeare', 'C. Proust', 3, 'Proust Il est connu pour son œuvre en prose "À la recherche du temps perdu".'
    ),
    (
        1, 'œuvre appartenant au mouvement surréaliste', 'A. Nadja', 'B. Les Champs Magnétiques', 'C. Du côté de chez Swann', 3, 'Du côté de chez Swann est une partie de l''œuvre de Marcel Proust, qui est surréaliste.'
    ),
    (
        1, 'roman gothique', 'A. Dracula', 'B. Frankenstein', 'C. Orgueil et Préjugés', 3, 'Orgueil et Préjugés est un roman de Jane Austen appartenant à la littérature romantique anglaise.'
    ),
    (
        1, 'œuvre écrite pendant la période de la Renaissance', 'A. Hamlet', 'B. La Divine Comédie', 'C. Utopia', 2, 'La Divine Comédie Écrite par Dante Alighieri, elle précède la Renaissance.'
    ),
    (
        1, 'poète appartenant au mouvement romantique', 'A. Lord Byron', 'B. John Keats', 'C. Charles Baudelaire', 3, 'Charles Baudelaire Il est souvent associé au symbolisme et au modernisme, bien qu''influencé par le romantisme.'
    ),
    (
        1, 'auteur qui a écrit de tragédie', 'A. Sophocle', 'B. Euripide', 'C. Voltaire', 3, 'Voltaire Bien qu''auteur de nombreux genres, il est principalement connu pour ses œuvres philosophiques.'
    ),
    (
        1, 'œuvre dystopique', 'A. 1984', 'B. Le Meilleur des mondes', 'C. À la recherche du temps perdu', 3, 'À la recherche du temps perdu est un roman de Marcel Proust explorant la psychologie et la mémoire.'
    ),
    (
        1, 'écrivain associé à la Beat Generation', 'A. Jack Kerouac', 'B. Allen Ginsberg', 'C. Ernest Hemingway', 3, 'Ernest Hemingway Il était un écrivain de la Génération Perdue, antérieure à la Beat Generation.'
    );
INSERT INTO
    questions (
        category_id, text, option1, option2, option3, correct_option, explication
    )
VALUES (
        2, 'langage de programmation fonctionnel ', 'A. Haskell', 'B. Lisp', 'C. Java',  3, 'Java est un langage de programmation impératif, pas fonctionnel.'
    ),
    (
        2, 'système d''exploitation destiné aux appareils mobiles ', 'A. Android', 'B. iOS', 'C. Ubuntu',  3, 'Ubuntu est un système d''exploitation pour ordinateurs de bureau et serveurs, pas pour les appareils mobiles.'
    ),
    (
        2, 'format de données principalement utilisé pour représenter des documents structurés ', 'A. JSON', 'B. XML', 'C. CSV',  3, 'CSV est principalement utilisé pour représenter des données tabulaires, pas des documents structurés.'
    ),
    (
        2, 'protocole de communication orienté connexion ', 'A. TCP', 'B. UDP', 'C. HTTP', 2, 'UDP est un protocole non orienté connexion.'
    ),
    (
        2, 'langage de script utilisé principalement pour l''automatisation des tâches système ', 'A. Bash', 'B. PowerShell', 'C. Python',  3, 'Python est utilisé pour une variété de tâches, y compris l''automatisation des tâches système, mais il  spécifiquement conçu pour cela.'
    ),
    (
        2, 'langage de programmation couramment utilisé pour l''analyse statistique et scientifique ', 'A. MATLAB', 'B. R', 'C. Java',  3, 'Java n''est pas aussi couramment utilisé que MATLAB et R pour l''analyse statistique et scientifique.'
    ),
    (
        2, 'composant matériel associé à un ordinateur ', 'A. RAM', 'B. GPU', 'C. Arduino',  3, 'Arduino est une plateforme de prototypage électronique, pas un composant matériel d''ordinateur.'
    ),
    (
        2, 'opération relationnelle SQL standard ', 'A. SELECT', 'B. INSERT', 'C. LOOP',  3, 'LOOP n''est pas une opération relationnelle standard en SQL.'
    ),
    (
        2, 'contrainte de base de données utilisée pour garantir l''intégrité des données ', 'A. Primary Key', 'B. Foreign Key', 'C. Index',  3, 'Un index est utilisé pour améliorer les performances des requêtes, pas pour garantir l''intégrité des données.'
    ),
    (
        2, 'entreprise associée à un système d''exploitation ', 'A. Microsoft', 'B. Apple', 'C. Intel',  3, 'Intel est une société de technologie qui fabrique des processeurs, pas un système d''exploitation.'
    );

INSERT INTO
    categories (
        id, name
    )
VALUES (1,"Litterature"
        ),
        (2,"Informatique"
        );

    