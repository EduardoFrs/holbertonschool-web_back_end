-- orm > sql
-- commentaire


SELECT
    band_name,
    CASE
        WHEN split IS NOT NULL THEN split - formed
        ELSE 2024 - formed
    END as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
