I=imread('6.jpeg')
imshow(I)
[x,y]=ginput(2)

z=1010.6;
fy=952.7;
fx=960.3;
x1=z*(x(1)/fx);
x2=z*(x(2)/fx);
y1=z*(y(1)/fy);
y2=z*(y(2)/fy);
dist=sqrt((y2-y1)^2+(x2-x1)^2);
fprintf('The distqance is %.02f mm',dist);