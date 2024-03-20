-- Insérer les nouvelles questions pour la catégorie Informatique
INSERT INTO
    questions (
        category_id, text, option1, option2, option3, correct_option
    )
VALUES (
        1, 'Identifiez l''intrus parmi :', 'Java', 'Python', 'Pomme', 3
    ),
    (
        1, 'Quel choix est l''intrus ?', 'HTML', 'CSS', 'Carotte', 3
    ),
    (
        1, 'Trouvez celui qui ne convient pas :', 'RAM', 'CPU', 'Poisson', 3
    ),
    (
        1, 'Choisissez l''intrus parmi :', 'Linux', 'Windows', 'Banane', 3
    ),
    (
        1, 'Lequel ne fait pas partie du groupe ?', 'PNG', 'JPEG', 'Avocat', 3
    ),
    (
        1, 'Identifiez l''intrus :', 'Facebook', 'Twitter', 'Brocoli', 3
    ),
    (
        1, 'Quel élément ne correspond pas ?', 'Router', 'Switch', 'Pomme', 3
    ),
    (
        1, 'Trouvez l''intrus parmi :', 'SQL', 'MongoDB', 'Fraise', 3
    ),
    (
        1, 'Lequel ne correspond pas au groupe ?', 'URL', 'API', 'Tomate', 3
    ),
    (
        1, 'Choisissez l''intrus :', 'Firewall', 'Antivirus', 'Salade', 3
    );

-- Insérer les nouvelles questions pour la catégorie Histoire
INSERT INTO
    questions (
        category_id, text, option1, option2, option3, correct_option
    )
VALUES (
        2, 'Sélectionnez l''intrus :', 'Révolution française', 'Révolution américaine', 'Avion', 3
    ),
    (
        2, 'Trouvez l''intrus :', 'Première Guerre mondiale', 'Seconde Guerre mondiale', 'Banane', 3
    ),
    (
        2, 'Quel élément ne correspond pas ?', 'Napoléon Bonaparte', 'Winston Churchill', 'Pizza', 3
    ),
    (
        2, 'Lequel ne convient pas au groupe ?', 'Tour Eiffel', 'Pyramides de Gizeh', 'Pomme', 3
    ),
    (
        2, 'Choisissez l''intrus :', 'Marie Curie', 'Charles Darwin', 'Voiture', 3
    ),
    (
        2, 'Identifiez l''intrus parmi :', 'Gandhi', 'Nelson Mandela', 'Brocoli', 3
    ),
    (
        2, 'Quel élément ne correspond pas ?', 'Chute de l''Empire romain', 'Découverte de l''Amérique', 'Fraise', 3
    ),
    (
        2, 'Trouvez l''intrus :', 'Empire Ottoman', 'Empire state building', 'Avion', 3
    ),
    (
        2, 'Lequel ne fait pas partie du groupe ?', 'Guerre de Cent Ans', 'Guerre des Roses', 'Salade', 3
    ),
    (
        2, 'Identifiez l''intrus parmi :', 'Louis XIV', 'Henri VIII', 'Cléopâtre', 3
    );

    -- Insérer de nouvelles catégories en fonction des questions existantes
INSERT INTO
    categories (name)
SELECT DISTINCT
    category_name
FROM (
        SELECT 'Informatique' AS category_name
        UNION
        SELECT 'Histoire' AS category_name
            -- Ajoutez d'autres catégories ici en fonction de vos questions
    ) AS temp
WHERE
    NOT EXISTS (
        SELECT 1
        FROM categories
        WHERE
            name = temp.category_name
    );