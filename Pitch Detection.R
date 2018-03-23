#Paul Boersma, Accurate short-term analysis of the fundamental frequency and the harmonics-to-noise ratio of a sampled sound, Institute of Phonetic Sciences,
#University of Amsterdam, Proceedings 17 (1993), 97-110.
T=0.024
t=seq(by=0.0001, from=0, to=T)
x=(1+0.3*sin(2*pi*140*t))*sin(2*pi*280*t)
#plot(t,x,'l')
u=mean(x)
w=0.5-0.5*cos(2*pi*t/T)
a=(x-u)*w
#plot(t,w,'l')
#plot(t,a,'l')
ra=1
for(tao in 1:(T*10000-1)){
    s=0
    for(k in 1:(T*10000-tao)){
        s=a[k]*a[k+tao]+s
    }
    s=s/sum(a^2)
    ra=c(ra,s)
}
ra=c(ra,0)
rw=(1-t/T)*(2/3+1/3*cos(2*pi*t/T)+1/(2*pi)*sin(2*pi*t/T))
rx=ra/rw
#plot(t,ra,'l')
#plot(t,rw,'l')
#plot(t,rx,'l')
