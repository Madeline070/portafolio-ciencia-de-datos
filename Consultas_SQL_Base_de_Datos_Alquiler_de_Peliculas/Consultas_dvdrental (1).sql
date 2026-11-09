/*
ACTIVIDAD: ANÁLISIS DE DATOS CON SQL
Base de datos: dvdrental
Instrucciones: Ejecuta cada ejercicio por separado. Para cada uno, selecciona
únicamente su consulta (sin seleccionar las consultas de los demás ejercicios)
y presiona F5. Toma una captura donde se vea la consulta y su resultado.
*/

USE dvdrental;
GO

-- 1. Vamos a seleccionar el nombre y apellido de los actores
SELECT first_name, last_name
FROM dbo.actor;
GO

-- 2. Vamos a seleccionar el nombre completo del actor en una sola columna
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo
FROM dbo.actor;
GO

-- 3. Selecciona los actores que su nombre empieza con "D"
SELECT first_name, last_name
FROM dbo.actor
WHERE first_name LIKE 'D%';
GO

-- 4. ¿Tenemos algún actor con el mismo nombre?
-- Muestra los nombres que aparecen más de una vez.
SELECT first_name, COUNT(*) AS cantidad
FROM dbo.actor
GROUP BY first_name
HAVING COUNT(*) > 1
ORDER BY cantidad DESC, first_name;
GO

-- 5. ¿Cuál es el costo máximo de renta de una película?
SELECT MAX(rental_rate) AS costo_maximo_renta
FROM dbo.film;
GO

-- 6. ¿Cuáles son las películas que fueron rentadas con ese costo?
SELECT title, rental_rate
FROM dbo.film
WHERE rental_rate = (SELECT MAX(rental_rate) FROM dbo.film)
ORDER BY title;
GO

-- 7. ¿Cuántas películas hay por el tipo de audiencia (rating)?
SELECT rating, COUNT(*) AS cantidad_peliculas
FROM dbo.film
GROUP BY rating
ORDER BY rating;
GO

-- 8. Selecciona las películas que no tienen un rating R o NC-17
SELECT title, rating
FROM dbo.film
WHERE rating NOT IN ('R', 'NC-17')
ORDER BY title;
GO

-- 9. ¿Cuántos clientes hay en cada tienda?
SELECT store_id, COUNT(*) AS cantidad_clientes
FROM dbo.customer
GROUP BY store_id
ORDER BY store_id;
GO

-- 10. ¿Cuál es la película que más veces se rentó?
SELECT TOP (1) WITH TIES
       f.title,
       COUNT(*) AS veces_rentada
FROM dbo.rental AS r
INNER JOIN dbo.inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN dbo.film AS f ON i.film_id = f.film_id
GROUP BY f.film_id, f.title
ORDER BY COUNT(*) DESC;
GO

-- 11. ¿Qué películas no se han rentado?
SELECT f.film_id, f.title
FROM dbo.film AS f
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.inventory AS i
    INNER JOIN dbo.rental AS r ON r.inventory_id = i.inventory_id
    WHERE i.film_id = f.film_id
)
ORDER BY f.title;
GO

-- 12. ¿Qué clientes no han rentado ninguna película?
SELECT c.customer_id, c.first_name, c.last_name
FROM dbo.customer AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.rental AS r
    WHERE r.customer_id = c.customer_id
)
ORDER BY c.last_name, c.first_name;
GO

-- 13. ¿Qué actores han actuado en más de 30 películas?
SELECT a.actor_id, a.first_name, a.last_name,
       COUNT(*) AS cantidad_peliculas
FROM dbo.actor AS a
INNER JOIN dbo.film_actor AS fa ON a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
HAVING COUNT(*) > 30
ORDER BY cantidad_peliculas DESC, a.last_name, a.first_name;
GO










USE dvdrental;
GO

-- EJERCICIO 14: Mostrar las ventas totales por tienda
SELECT
    st.store_id,
    SUM(TRY_CONVERT(DECIMAL(10,2), p.amount)) AS ventas_totales
FROM dbo.payment AS p
INNER JOIN dbo.staff AS st
    ON p.staff_id = st.staff_id
GROUP BY st.store_id
ORDER BY st.store_id;













































-- 15. Muestra los clientes que rentaron una película más de una vez
-- Lista cada cliente y película cuando ese cliente rentó esa película
-- en más de una ocasión.

USE dvdrental;
GO

-- EJERCICIO 15: Clientes que rentaron la misma película más de una vez
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    f.title AS pelicula,
    COUNT(*) AS veces_rentada
FROM dbo.rental AS r
INNER JOIN dbo.customer AS c
    ON r.customer_id = c.customer_id
INNER JOIN dbo.inventory AS i
    ON r.inventory_id = i.inventory_id
INNER JOIN dbo.film AS f
    ON i.film_id = f.film_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    f.film_id,
    f.title
HAVING COUNT(*) > 1
ORDER BY veces_rentada DESC;

