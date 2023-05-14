KendallW <- function(x, y) {
  # convert x and y to nemeric type
    x<-as.numeric(x)
    y<-as.numeric(y)
  res<-cor.test(x,y, method="kendall")
  print(class(res))
  # convert w to numeric type
    res<-as.numeric(res$estimate)
  # remove [1] from the result
    res<-res[1]
  return(res)
}
x<-c(1,2,3,2,1,3,4,2,5,2,6,5,5)
y<-c(5,5,6,2,1,4,4,2,1,2,1,5,5)

print(KendallW(x,y))



