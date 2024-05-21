UPDATE country_vaccination_stats AS v1 
SET daily_vaccinations = COALESCE(SELECT DISTINCT PERCENTILE_CONT(0.5) 
WITHIN GROUP(ORDER BY daily_vaccinations) OVER (PARTITION BY country), 0) 
WHERE daily_vaccinations IS NULL; 