package antikythera.time;

/**
 * Created by Nick on 1/14/14.
 */
public abstract class TimeSpecification {
    public TimeSpecification(String json)
    {
        parse(json);
    }

    public abstract void parse(String json);
}
