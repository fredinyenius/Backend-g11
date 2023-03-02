CREATE TABLE alumnos_cursos(
    id SERIAL PRIMARY KEY,
    alumnos_id INT NOT NULL,
    cursos_id INT NOT NULL,
    UNIQUE (alumnos_id, cursos_id),
    CONSTRAINT fk_alumnos FOREIGN KEY (alumnos_id) REFERENCES alumnos(id),
    CONSTRAINT fk_cursos FOREIGN KEY (cursos_id) REFERENCES cursos(id)
);


INSERT INTO cursos (nombre, descripcion, habilitado) VALUES
                    ('Matematica', 'Matematica con algebra', true),
                    ('CTA', 'Cienta Tecnologia y Ambiente', true),
                    ('Comunicacion', 'Letras', true),
                    ('Arte', 'Artes plasticas', false),
                    ('Ingles', 'English for kids', true);

INSERT INTO alumnos_cursos (alumnos_id, cursos_id) VALUES
                               (1,     1),
                               (2,     1),
                               (1,     3),
                               (3,     4),
                               (3,     2),
                               (3,     3);

--HACER UN INER JOIN JOIN ENTRE LA TABLA ALUMNOS Y LA TA

SELECT * FROM alumnos  
inner join alumnos_cursos  ON
 alumnos_id=alumnos_id;


SELECT * FROM cursos 
inner join alumnos_cursos  ON
cursos_id=cursos_id;

SELECT alumnos.nombre, alumnos.apellido FROM alumnos_cursos inner join
alumnos ON alumnos_id = alumnos_id inner join
 cursos ON cursos_id = cursos_id
 where cursos.nombre = 'Comunicacion';

 