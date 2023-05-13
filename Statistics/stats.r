KendallW <- function(x, y, na.rm = FALSE) {
  if (na.rm) {
    x <- x[!is.na(x)]
    y <- y[!is.na(y)]
  }
  n <- length(x)
  if (n != length(y)) {
    stop("x and y must have the same length")
  }
  if (n < 2) {
    stop("x and y must have at least 2 observations")
  }
  if (any(is.na(x)) || any(is.na(y))) {
    warning("NAs introduced by coercion")
  }
  x <- as.numeric(x)
  y <- as.numeric(y)
  if (any(is.na(x)) || any(is.na(y))) {
    stop("x and y must be coercible to numeric")
  }
  if (any(duplicated(x)) || any(duplicated(y))) {
    warning("some observations with the same value were omitted")
  }
  x <- rank(x)
  y <- rank(y)
  W <- sum((x - mean(x)) * (y - mean(y)))
  W <- W / (n * (n - 1) / 2)
  return(W)
}
# print (KendallW(c(1,2,3,4,5),c(1,0,11,4,2)))
