for f in *
do
    mv "$f" "$(echo $f | sed 's@_2012@_12@g' | sed 's@Beam.*MagDown@MagDown@g' | sed 's@Down.*DST@Down.py@g' | sed 's@Beam.*MagUp@MagUp@g' | sed 's@Up.*DST@Up.py@g')"
done

for f in *
do
    mv "$f" "$(echo $f | sed 's@MagUp@MagUp.py@g')"
done
    
	    



    
      
