library(tidyverse)
library(hrbrthemes)

plot <- read_csv("occupations.csv") %>%
  pivot_longer(!year, names_to="occupation", values_to="time") %>%
  ggplot(aes(x=year, y=time)) +
  geom_bar(aes(fill=occupation), stat="identity") +
  theme_ipsum() +
  scale_fill_ipsum()
ggsave(filename="occupations.jpg", plot=plot, width=1800, height=1000, units="px")